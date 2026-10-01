import Fuse from 'fuse.js'
import entries from '../data/entries.json'
import { byName } from './categories'

// Same normalization for the typed text and for the data:
// lowercase, strip accents (š→s, č/ć→c, ž→z), đ→dj, trim extra spaces.
export function normalize(text = '') {
  return text
    .toLowerCase()
    .replace(/đ/g, 'dj')
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9 ]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

export const entryById = Object.fromEntries(entries.map((e) => [e.id, e]))
export const allEntries = entries

// Penalty added per kind of match so main matches rank above side matches.
const KIND_PENALTY = { english: 0, main: 0, meaning: 0.04, texting: 0.03, form: 0.03, alt: 0.05, ijekavian: 0.05, tag: 0.12 }

function buildDocs() {
  const docs = []
  const add = (entry, text, kind, note) => {
    const n = normalize(text)
    if (n) docs.push({ id: entry.id, text: n, kind, note })
  }
  for (const e of entries) {
    add(e, e.english, 'english')
    add(e, e.serbian, 'main')
    add(e, e.meaning, 'meaning')
    add(e, e.literal, 'meaning')
    // texting can be "hvala / fala": index each piece
    ;(e.texting || '').split('/').forEach((t) => add(e, t, 'texting', `texting spelling of ${e.english}`))
    add(e, e.ijekavian, 'ijekavian', `ijekavian spelling of ${e.serbian}`)
    for (const f of e.forms || []) add(e, f.serbian, 'form', `${f.serbian} (${f.useWhen.toLowerCase()} · ${e.english})`)
    for (const a of e.alternatives || []) add(e, a.serbian, 'alt', `${a.serbian} (another way to say ${e.english})`)
    for (const t of e.tags || []) add(e, t, 'tag', `tagged "${t}"`)
    add(e, e.category, 'tag')
    add(e, e.subcategory, 'tag')
  }
  return docs
}

const docs = buildDocs()
const fuseOptions = { keys: ['text'], includeScore: true, ignoreLocation: true, threshold: 0.35, minMatchCharLength: 2 }
const fuse = new Fuse(docs, fuseOptions)
const looseFuse = new Fuse(docs, { ...fuseOptions, threshold: 0.55 })

function collapse(rawResults, query) {
  const best = new Map()
  for (const r of rawResults) {
    const { id, text, kind, note } = r.item
    let score = (r.score ?? 0) + KIND_PENALTY[kind]
    if (text === query) score -= 0.2
    else if (text.startsWith(query)) score -= 0.1
    else if (text.split(' ').some((w) => w.startsWith(query))) score -= 0.05
    const current = best.get(id)
    if (!current || score < current.score) best.set(id, { id, score, note: kind === 'form' || kind === 'alt' || kind === 'texting' || kind === 'ijekavian' || kind === 'tag' ? note : null })
  }
  const sorted = [...best.values()].sort((a, b) => a.score - b.score)
  // Drop weak matches far behind the best one.
  const kept = sorted.filter((r) => r.score <= sorted[0].score + 0.2)
  return kept.map((r) => ({ entry: entryById[r.id], note: r.note }))
}

export function search(rawQuery, { limit = 20 } = {}) {
  const q = normalize(rawQuery)
  if (!q) return { results: [], suggestions: [] }
  // Substring hits always count, even for very short queries; Fuse adds typo tolerance.
  const matches = q.length < 2 ? (d) => d.text.split(' ').some((w) => w.startsWith(q)) : (d) => d.text.includes(q)
  const substring = docs.filter(matches).map((item) => ({ item, score: 0 }))
  const fuzzy = q.length >= 3 ? fuse.search(q) : []
  const results = collapse([...substring, ...fuzzy], q).slice(0, limit)
  if (results.length) return { results, suggestions: [] }
  const suggestions = q.length >= 2 ? collapse(looseFuse.search(q), q).slice(0, 4) : []
  return { results: [], suggestions }
}

export const categoryOf = (entry) => byName(entry.category)

import words from '../data/words.json'
import entries from '../data/entries.json'

// Split a Serbian line into plain text and tappable words. Multi-word chunks ("laku noć", "majke mi") win over
// single words; anything in (parentheses) is an English note and stays plain.
const WORD = /l'|[\p{L}\p{M}]+/gu
const CHUNK_MAX = 3

export const wordKey = (s) => s.toLowerCase().replace(/’/g, "'").trim()
export const lookupWord = (key) => words[wordKey(key)]
export const wordCount = Object.keys(words).length

export function tokenize(text = '') {
  const out = []
  const plain = (t) => { if (t) out.push({ text: t }) }
  // Walk the string, skipping (…) groups.
  const parts = text.split(/(\([^)]*\))/)
  for (const part of parts) {
    if (part.startsWith('(')) { plain(part); continue }
    const matches = [...part.matchAll(WORD)]
    let cursor = 0
    for (let i = 0; i < matches.length; i++) {
      const m = matches[i]
      let used = 1
      let key = wordKey(m[0])
      // Longest chunk first: join following words only if just spaces separate them.
      for (let n = Math.min(CHUNK_MAX, matches.length - i); n >= 2; n--) {
        const span = matches.slice(i, i + n)
        const joined = span.map((x) => x[0]).join(' ')
        const raw = part.slice(m.index, span[n - 1].index + span[n - 1][0].length)
        if (raw.replace(/\s+/g, ' ') === joined && words[wordKey(joined)]) { key = wordKey(joined); used = n; break }
      }
      const last = matches[i + used - 1]
      plain(part.slice(cursor, m.index))
      const shown = part.slice(m.index, last.index + last[0].length)
      if (words[key]) out.push({ text: shown, key })
      else plain(shown)
      cursor = last.index + last[0].length
      i += used - 1
    }
    plain(part.slice(cursor))
  }
  return out
}

// Built on first use: for each word, which entries use it, one short example line, and its other forms
// (words whose card says "Locative of X", "Ijekavian of X"… point back to X).
let index
function buildIndex() {
  const usedIn = new Map(), example = new Map(), family = new Map()
  for (const [k, w] of Object.entries(words)) if (w.base) family.set(w.base, [...(family.get(w.base) || []), k])
  // rank: 0 = in the entry's own phrase, 1 = in one of its alternatives or forms, 2 = only in an example sentence
  const seen = (key, id, rank) => {
    const m = usedIn.get(key) || usedIn.set(key, new Map()).get(key)
    if (!m.has(id) || m.get(id) > rank) m.set(id, rank)
  }
  for (const e of entries) {
    const tiers = [
      [0, [e.serbian]],
      [1, [...(e.alternatives || []).map((a) => a.serbian), ...(e.forms || []).map((f) => f.serbian)]],
      [2, [...e.examples, ...(e.forms || []).map((f) => f.example).filter(Boolean)].map((x) => x.serbian)],
    ]
    for (const [rank, lines] of tiers) for (const t of lines) for (const p of tokenize(t)) if (p.key) seen(p.key, e.id, rank)
    for (const x of [...e.examples, ...(e.forms || []).map((f) => f.example).filter(Boolean)]) for (const p of tokenize(x.serbian)) {
      if (!p.key) continue
      const cur = example.get(p.key)
      if (!cur || x.serbian.length < cur.serbian.length) example.set(p.key, x)
    }
  }
  index = { usedIn, example, family }
}

export function wordInfo(key) {
  if (!index) buildIndex()
  const w = words[key]
  const used = [...(index.usedIn.get(key) || new Map())].sort((a, b) => a[1] - b[1]).map(([id]) => id).filter((id) => id !== w?.entry)
  return { used, example: index.example.get(key) || null, forms: (index.family.get(key) || []).filter((k) => k !== key) }
}

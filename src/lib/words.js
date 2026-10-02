import words from '../data/words.json'

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

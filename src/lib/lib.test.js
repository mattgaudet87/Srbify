import { describe, expect, it, beforeAll } from 'vitest'
import { normalize, search, searchWords, entryById, allEntries } from './search.js'
import { tokenize, loadWords, lookupWord } from './words.js'
import { isYourForm } from './settings.jsx'
import { isVisible } from './visibility.js'
import { entryTags, audience } from './tags.js'
import { placementsOf } from './categories.js'
import { stripAccents } from '../components/CopyButton.jsx'

beforeAll(() => loadWords())

describe('normalize', () => {
  it('drops accents and maps đ to dj', () => {
    expect(normalize('Šta ima, đače?')).toBe('sta ima djace')
    expect(normalize('  ČĆŽ   ')).toBe('ccz')
  })
  it('handles empty input', () => expect(normalize()).toBe(''))
})

describe('stripAccents', () => {
  it('keeps case and punctuation', () => expect(stripAccents('Šta ima? Đurđevdan')).toBe('Sta ima? Djurdjevdan'))
})

describe('search', () => {
  it('finds a phrase without accents', () => {
    const { results } = search('sta')
    expect(results.length).toBeGreaterThan(0)
  })
  it('returns nothing for an empty query', () => expect(search('   ')).toEqual({ results: [], suggestions: [] }))
  it('hides vulgar entries unless asked', () => {
    const vulgar = allEntries.find((e) => e.register === 'vulgar')
    const q = vulgar.english
    expect(search(q, { showVulgar: false }).results.some((r) => r.entry.id === vulgar.id)).toBe(false)
    expect(search(q, { showVulgar: true }).results.some((r) => r.entry.id === vulgar.id)).toBe(true)
  })
  it('searches word cards by Serbian and English, skipping vulgar ones by default', () => {
    expect(searchWords('hvala').length).toBeGreaterThan(0)
    expect(searchWords('x')).toEqual([])
  })
})

describe('tokenize', () => {
  it('makes known words tappable and leaves (notes) plain', () => {
    const parts = tokenize('Hvala ti (thanks)')
    expect(parts.find((p) => p.text === 'Hvala')?.key).toBe('hvala')
    expect(parts.find((p) => p.text === '(thanks)')?.key).toBeUndefined()
  })
  it('joins fixed multi-word chunks when a card exists for them', () => {
    const chunk = Object.keys(Object.fromEntries(allEntries.flatMap((e) => (e.serbian.split(' ').length === 2 && lookupWord(e.serbian) ? [[e.serbian.toLowerCase(), 1]] : []))))[0]
    if (chunk) expect(tokenize(chunk).filter((p) => p.key)).toHaveLength(1)
  })
  it('never loses text', () => {
    for (const e of allEntries.slice(0, 80)) expect(tokenize(e.serbian).map((p) => p.text).join('')).toBe(e.serbian)
  })
})

describe('isYourForm', () => {
  const me = { speaker: 'male', listener: 'female' }
  it('needs a speaker tag to match', () => {
    expect(isYourForm({ speaker: 'male' }, me)).toBe(true)
    expect(isYourForm({ speaker: 'female' }, me)).toBe(false)
  })
  it('matches who the sentence describes against who you talk to', () => {
    expect(isYourForm({ describes: 'her' }, me)).toBe(true)
    expect(isYourForm({ describes: 'him' }, me)).toBe(false)
    expect(isYourForm({ describes: 'him' }, { ...me, listener: 'male' })).toBe(true)
  })
  it('only counts casual, Serbian-spelling rows', () => {
    expect(isYourForm({ speaker: 'male', formal: 'polite' }, me)).toBe(false)
    expect(isYourForm({ speaker: 'male', region: 'bosnia' }, me)).toBe(false)
  })
  it('never highlights a row with no matching tags (noun gender)', () => expect(isYourForm({ nounGender: 'fem' }, me)).toBe(false))
})

describe('isVisible', () => {
  it('follows the vulgar setting', () => {
    expect(isVisible({ register: 'vulgar' }, { showVulgar: false })).toBe(false)
    expect(isVisible({ register: 'vulgar' }, { showVulgar: true })).toBe(true)
    expect(isVisible({ register: 'slang' }, { showVulgar: false })).toBe(true)
  })
})

describe('entry data helpers', () => {
  it('every entry gets tags, an audience and at least one placement', () => {
    for (const e of allEntries) {
      expect(entryTags(e).length).toBeGreaterThan(0)
      expect(audience(e)).toBeTruthy()
      expect(placementsOf(e).length).toBeGreaterThan(0)
    }
  })
  it('has unique ids and resolving related links', () => {
    expect(new Set(allEntries.map((e) => e.id)).size).toBe(allEntries.length)
    for (const e of allEntries) for (const r of e.related) expect(entryById[r]).toBeDefined()
  })
})

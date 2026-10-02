import { placementsOf } from './categories.js'

// Scannable tags, worked out from the entry's own data so they never drift out of sync.
// kind: tone (how it sounds) · tense · gender (does M/F matter) · change (other ways it changes)
const TONE = { casual: 'Casual', neutral: 'Neutral', slang: 'Slang', vulgar: 'Vulgar' }
const CHANGE_LABELS = {
  plural: 'Changes for groups',
  formal: 'Casual / polite form',
  tense: 'Past tense changes',
  addressing: 'Form when calling her this',
  region: 'Regional spelling',
}

export function entryTags(e) {
  const out = []
  const add = (key, label, kind, long) => out.push({ key, label, kind, long: long || label })
  const subs = placementsOf(e).map((p) => p.subcategory)
  const flirty = e.tags.includes('flirty')
  const formal = e.tags.includes('polite') || subs.includes('Formal and polite')

  if (formal) add('formal', 'Formal', 'tone', 'Formal / polite')
  if (flirty) add('flirty', 'Flirty', 'tone')
  if (e.register === 'neutral' ? !formal && !flirty : true) add(e.register, TONE[e.register], 'tone')

  for (const t of ['past', 'present', 'future']) if (e.tags.includes(t) || subs.includes(t[0].toUpperCase() + t.slice(1))) add(t, t[0].toUpperCase() + t.slice(1), 'tense', `${t[0].toUpperCase() + t.slice(1)} tense`)

  const by = e.changesBy
  if (by.includes('speaker')) add('mf-speaker', 'M/F: you', 'gender', 'Changes if you’re M / F')
  if (by.includes('describes')) add('mf-about', 'M/F: them', 'gender', 'Changes by who it describes')
  if (by.includes('noun gender')) add('noun-gender', 'Noun gender', 'gender', 'Matches the noun')
  for (const c of by) if (CHANGE_LABELS[c]) add(c, c === 'tense' ? 'Tense' : c[0].toUpperCase() + c.slice(1), 'change', CHANGE_LABELS[c])
  if (!by.length) add('never', 'Never changes', 'change')
  if (e.texting && (e.tags.includes('texting') || e.tags.includes('abbreviation'))) add('texting', 'Texting', 'tone')
  return out
}

export const tagFilterLabel = { formal: 'Formal', flirty: 'Flirty', casual: 'Casual', neutral: 'Neutral', slang: 'Slang', vulgar: 'Vulgar', texting: 'Texting',
  past: 'Past', present: 'Present', future: 'Future', 'mf-speaker': 'M/F: you', 'mf-about': 'M/F: them', 'noun-gender': 'Noun gender', plural: 'Plural', never: 'Never changes' }

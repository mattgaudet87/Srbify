import Icon from './Icons.jsx'
import { entryTags } from '../lib/tags.js'

const CHANGE_LABELS = {
  speaker: 'Changes if you’re M / F',
  describes: 'Changes by who it describes',
  'noun gender': 'Matches the noun',
  plural: 'Changes for groups',
  formal: 'Casual / polite form',
  tense: 'Past tense changes',
  addressing: 'Form when calling her this',
  region: 'Regional spelling',
}

export function RegisterBadge({ register }) {
  return <span className={`badge reg-${register}`}>{register[0].toUpperCase() + register.slice(1)}</span>
}

export function ChangeBadges({ entry, max = 3 }) {
  if (!entry.changesBy.length) return <span className="badge never">Never changes</span>
  return entry.changesBy.slice(0, max).map((c) => (
    <span key={c} className="badge changes">{CHANGE_LABELS[c] || c}</span>
  ))
}

// Blue = a native speaker verified it, or Claude is confident. Gray = needs checking (the reason is in reviewNote).
export const confidenceOf = (e) => (e.verified ? 'verified' : e.confidence === 'unsure' ? 'unsure' : 'sure')
const CONFIDENCE = {
  verified: { icon: 'check', label: 'Verified by a native speaker', short: 'Verified' },
  sure: { icon: 'check', label: 'Confident · not yet checked by a native speaker', short: 'Confident' },
  unsure: { icon: 'shield', label: 'Needs checking', short: 'Needs checking' },
}

export function ConfidenceBadge({ entry }) {
  const level = confidenceOf(entry), c = CONFIDENCE[level]
  return (
    <>
      <span className={`badge conf conf-${level}`}><Icon name={c.icon} size={14} strokeWidth={2.4} />{c.label}</span>
      {level === 'unsure' && entry.reviewNote && <p className="review-note"><strong>To double-check:</strong> {entry.reviewNote}</p>}
    </>
  )
}

// Tiny corner mark for list rows.
export function ConfidenceMark({ entry }) {
  const level = confidenceOf(entry), c = CONFIDENCE[level]
  return <span className={`conf-mark conf-${level}`} role="img" aria-label={c.label} title={c.label}><Icon name={c.icon} size={13} strokeWidth={2.6} /></span>
}

// Small coloured tags: tone, tense, who it changes for. `max` trims for list rows; `long` uses the full labels.
export function TagPills({ entry, max = 99, long = false, kinds }) {
  const tags = entryTags(entry).filter((t) => !kinds || kinds.includes(t.kind)).slice(0, max)
  return tags.map((t) => <span key={t.key} className={`tag tag-${t.kind} t-${t.key}`}>{long ? t.long : t.label}</span>)
}

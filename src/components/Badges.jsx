import Icon from './Icons.jsx'
import { entryTags } from '../lib/tags.js'

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

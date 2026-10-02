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

export function VerifiedBadge({ verified }) {
  return (
    <span className={`badge ${verified ? 'verified' : 'unverified'}`}>
      <Icon name={verified ? 'check' : 'shield'} size={14} />
      {verified ? 'Verified by a native speaker' : 'Not yet verified'}
    </span>
  )
}

// Small coloured tags: tone, tense, who it changes for. `max` trims for list rows; `long` uses the full labels.
export function TagPills({ entry, max = 99, long = false, kinds }) {
  const tags = entryTags(entry).filter((t) => !kinds || kinds.includes(t.kind)).slice(0, max)
  return tags.map((t) => <span key={t.key} className={`tag tag-${t.kind} t-${t.key}`}>{long ? t.long : t.label}</span>)
}

import { Link } from 'react-router-dom'
import { RegisterBadge, ChangeBadges } from './Badges.jsx'

export default function EntryRow({ entry, note, category, onClick }) {
  return (
    <Link to={`/entry/${entry.id}`} className="row" onClick={onClick}>
      <span className="row-en">{entry.english}</span>
      <span className="row-sr">{entry.serbian}</span>
      <span className="row-pr">{entry.pronunciation}</span>
      {note && <span className="row-note">{note}</span>}
      {category && <span className="row-cat">{category}</span>}
      <span className="row-badges">
        {entry.register !== 'neutral' && <RegisterBadge register={entry.register} />}
        <ChangeBadges entry={entry} max={2} />
      </span>
    </Link>
  )
}

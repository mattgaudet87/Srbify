import { Link } from 'react-router-dom'
import Icon from './Icons.jsx'
import SpeakButton from './SpeakButton.jsx'
import StarButton from './StarButton.jsx'
import { TagPills, ConfidenceMark } from './Badges.jsx'

// One line in any list. `star` swaps the chevron for a favorite toggle.
export default function EntryRow({ entry, note, star = false }) {
  return (
    <div className="row-wrap">
      <Link to={`/entry/${entry.id}`} className="row">
        <span className="row-en">{entry.english}</span>
        <span className="row-sr">{entry.serbian}</span>
        <span className="row-pr">{entry.pronunciation}</span>
        {note && <span className="row-note">{note}</span>}
        <span className="row-tags"><TagPills entry={entry} max={4} /></span>
        <ConfidenceMark entry={entry} />
        {!star && <Icon name="chevronR" size={20} className="row-chev" />}
      </Link>
      <span className={`row-speak ${star ? 'with-star' : ''}`}><SpeakButton text={entry.serbian} iconOnly /></span>
      {star && <StarButton id={entry.id} className="row-star" />}
    </div>
  )
}

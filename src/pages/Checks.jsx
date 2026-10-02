import { Link } from 'react-router-dom'
import { allEntries } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import { isVisible } from '../lib/visibility.js'
import { ConfidenceMark } from '../components/Badges.jsx'
import CopyButton from '../components/CopyButton.jsx'
import Icon from '../components/Icons.jsx'

// Everything Claude flagged as "not sure", with what to check. Resolved items leave this list when a native speaker confirms them.
export default function Checks() {
  const { settings } = useSettings()
  const open = allEntries.filter((e) => e.confidence === 'unsure' && !e.verified && isVisible(e, settings))
  const text = open.map((e) => `${e.serbian} (${e.english}) [${e.id}]: ${e.reviewNote}`).join('\n')
  const sure = allEntries.length - allEntries.filter((e) => e.confidence === 'unsure' && !e.verified).length
  return (
    <>
      <Link to="/settings" className="back" aria-label="Back to Settings"><Icon name="chevronL" size={26} /></Link>
      <h1 className="title">To double-check</h1>
      <div className="checks-legend">
        <span><ConfidenceMark entry={{ confidence: 'sure' }} /> Blue: Claude is confident, or a native speaker verified it ({sure} entries)</span>
        <span><ConfidenceMark entry={{ confidence: 'unsure' }} /> Gray: needs checking ({open.length} shown below)</span>
      </div>
      <p className="hint">Pronunciation spellings and Ijekavian forms are approximations across the whole app and haven’t been checked by a native speaker.</p>
      {open.length > 0 && <CopyButton text={text} small label="Copy this list to send for checking" />}
      <div className="card-list">
        {open.map((e) => (
          <div key={e.id} className="row-wrap">
            <Link to={`/entry/${e.id}`} className="row">
              <span className="row-en">{e.english}</span>
              <span className="row-sr">{e.serbian}</span>
              <span className="row-note">{e.reviewNote}</span>
              <ConfidenceMark entry={e} />
            </Link>
          </div>
        ))}
        {!open.length && <p className="empty pad">Nothing to double-check right now.</p>}
      </div>
    </>
  )
}

import { Link } from 'react-router-dom'
import { CATEGORIES } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import { useLibrary } from '../lib/library.jsx'
import { entryById } from '../lib/search.js'
import EntryStrip from '../components/EntryStrip.jsx'

export default function Home() {
  const { settings } = useSettings()
  const visible = allEntries.filter((e) => settings.showVulgar || e.register !== 'vulgar')
  const { favorites } = useLibrary()
  const pick = (ids) => ids.map((id) => entryById[id]).filter((e) => e && (settings.showVulgar || e.register !== 'vulgar'))
  const hidden = allEntries.length - visible.length
  const counts = visible.reduce((acc, e) => ((acc[e.category] = (acc[e.category] || 0) + 1), acc), {})
  return (
    <>
      <h1 className="h1">Casual Serbian, fast</h1>
      <p className="lede">Search above, or pick a category.</p>
      {hidden > 0 && <p className="hint">{hidden} vulgar {hidden === 1 ? 'entry is' : 'entries are'} hidden. <Link to="/settings">Change in Settings</Link></p>}
      <EntryStrip title="★ Favorites" entries={pick(favorites)} />
      <div className="grid">
        {CATEGORIES.map((c) => {
          const n = counts[c.name] || 0
          return (
            <Link key={c.slug} to={`/category/${c.slug}`} className={`tile ${n ? '' : 'soon'}`}>
              <span className="tile-icon" aria-hidden="true">{c.icon}</span>
              <span className="tile-name">{c.name}</span>
              <span className="tile-count">{n ? `${n} ${n === 1 ? 'entry' : 'entries'}` : 'Coming soon'}</span>
            </Link>
          )
        })}
      </div>
    </>
  )
}

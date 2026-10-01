import { Link } from 'react-router-dom'
import { useLibrary } from '../lib/library.jsx'
import { useSettings } from '../lib/settings.jsx'
import { entryById } from '../lib/search.js'
import EntryRow from '../components/EntryRow.jsx'

export default function Favorites() {
  const { favorites } = useLibrary()
  const { settings } = useSettings()
  const entries = favorites.map((id) => entryById[id]).filter((e) => e && (settings.showVulgar || e.register !== 'vulgar'))
  return (
    <>
      <h1 className="title">Favorites</h1>
      {entries.length ? (
        <div className="card-list">{entries.map((e) => <EntryRow key={e.id} entry={e} star />)}</div>
      ) : (
        <p className="empty">Nothing starred yet. Tap the star on any phrase to keep it here. <Link to="/search">Find a phrase</Link></p>
      )}
    </>
  )
}

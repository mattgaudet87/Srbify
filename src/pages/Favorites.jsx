import { useState } from 'react'
import { Link } from 'react-router-dom'
import { useLibrary } from '../lib/library.jsx'
import { useSettings } from '../lib/settings.jsx'
import { entryById } from '../lib/search.js'
import { isVisible } from '../lib/visibility.js'
import EntryRow from '../components/EntryRow.jsx'
import CopyButton from '../components/CopyButton.jsx'

export default function Favorites() {
  const { favorites, setFavorites } = useLibrary()
  const { settings } = useSettings()
  const [sort, setSort] = useState('recent')
  const [code, setCode] = useState('')
  const [msg, setMsg] = useState('')
  const all = favorites.map((id) => entryById[id]).filter((e) => e && isVisible(e, settings))
  const entries = sort === 'az' ? [...all].sort((a, b) => a.english.localeCompare(b.english)) : all
  const backup = JSON.stringify(favorites)

  function restore() {
    try {
      const ids = JSON.parse(code)
      if (!Array.isArray(ids)) throw new Error('not a list')
      const valid = ids.filter((id) => typeof id === 'string' && entryById[id])
      const fresh = valid.filter((id) => !favorites.includes(id))
      setFavorites([...new Set([...valid, ...favorites])])
      setMsg(fresh.length ? `Added ${fresh.length} ${fresh.length === 1 ? 'favorite' : 'favorites'}.` : 'Those are all in your favorites already.')
      setCode('')
    } catch {
      setMsg('That code doesn’t look right. Paste the whole thing you copied.')
    }
  }
  function clearAll() {
    if (window.confirm(`Remove all ${all.length} favorites?`)) setFavorites(favorites.filter((id) => !all.some((e) => e.id === id)))
  }

  return (
    <>
      <h1 className="title">Favorites</h1>
      {entries.length ? (
        <>
          <div className="fav-tools">
            <Link to="/review" className="chip on">Practice these</Link>
            <button type="button" className={`chip ${sort === 'recent' ? 'on' : ''}`} onClick={() => setSort('recent')}>Newest</button>
            <button type="button" className={`chip ${sort === 'az' ? 'on' : ''}`} onClick={() => setSort('az')}>A to Z</button>
            <button type="button" className="chip" onClick={clearAll}>Clear all</button>
          </div>
          <div className="card-list">{entries.map((e) => <EntryRow key={e.id} entry={e} star />)}</div>
        </>
      ) : (
        <p className="empty">Nothing starred yet. Tap the star on any phrase to keep it here. <Link to="/search">Find a phrase</Link></p>
      )}
      <details className="backup">
        <summary>Back up or move your favorites</summary>
        <p className="hint">Favorites live only in this browser. Copy the code to keep a backup, or paste one here to restore it on another phone.</p>
        {favorites.length > 0 && <div className="fav-tools"><CopyButton text={backup} small label="Copy my backup code" /></div>}
        <textarea value={code} onChange={(e) => setCode(e.target.value)} placeholder="Paste a backup code here" aria-label="Backup code" />
        <div className="fav-tools"><button type="button" className="chip" disabled={!code.trim()} onClick={restore}>Restore</button>{msg && <span className="muted">{msg}</span>}</div>
      </details>
    </>
  )
}

import { useEffect, useMemo, useRef, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { search } from '../lib/search.js'
import EntryRow from './EntryRow.jsx'

export default function SearchBar() {
  const [query, setQuery] = useState('')
  const inputRef = useRef(null)
  const { pathname } = useLocation()
  const { results, suggestions } = useMemo(() => search(query), [query])
  const open = query.trim().length > 0

  // Close results whenever you navigate somewhere.
  useEffect(() => {
    setQuery('')
  }, [pathname])

  return (
    <header className="topbar">
      <div className="topbar-inner">
        <Link to="/" className="brand" aria-label="Srbify home">
          <img src="/logo-192.png" alt="" width="36" height="36" />
        </Link>
        <div className="search">
          <input
            ref={inputRef}
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search English or Serbian…"
            aria-label="Search"
            autoComplete="off"
            autoCapitalize="off"
            spellCheck="false"
          />
          {open && (
            <button className="clear" aria-label="Clear search" onClick={() => { setQuery(''); inputRef.current?.focus() }}>×</button>
          )}
        </div>
      </div>
      {open && (
        <div className="results" role="region" aria-label="Search results">
          {results.map(({ entry, note }) => (
            <EntryRow key={entry.id} entry={entry} note={note} category={entry.category} />
          ))}
          {!results.length && (
            <div className="no-match">
              <strong>No match yet</strong>
              {suggestions.length > 0 && <p>Closest suggestions:</p>}
              {suggestions.map(({ entry, note }) => (
                <EntryRow key={entry.id} entry={entry} note={note} category={entry.category} />
              ))}
            </div>
          )}
        </div>
      )}
    </header>
  )
}

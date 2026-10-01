import { useMemo, useState } from 'react'
import { search } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import EntryRow from '../components/EntryRow.jsx'
import FilterChips from '../components/FilterChips.jsx'
import Icon from '../components/Icons.jsx'

const isWord = (e) => !/\s/.test(e.serbian.trim())
const isSlang = (e) => e.register === 'slang' || e.register === 'vulgar'
const FILTERS = {
  all: () => true,
  phrases: (e) => !isWord(e),
  words: isWord,
  slang: isSlang,
}

export default function Search() {
  const [query, setQuery] = useState('')
  const [filter, setFilter] = useState('all')
  const { settings } = useSettings()
  const { results, suggestions } = useMemo(() => search(query, { showVulgar: settings.showVulgar, limit: 60 }), [query, settings.showVulgar])
  const open = query.trim().length > 0
  const count = (k) => results.filter((r) => FILTERS[k](r.entry)).length
  const shown = results.filter((r) => FILTERS[filter](r.entry))

  return (
    <>
      <h1 className="title">Search</h1>
      <div className="search-field">
        <Icon name="search" size={20} />
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search English or Serbian…"
          aria-label="Search"
          autoFocus
          autoComplete="off"
          autoCapitalize="off"
          spellCheck="false"
        />
        {open && <button className="clear" aria-label="Clear search" onClick={() => setQuery('')}><Icon name="x" size={14} strokeWidth={2.4} /></button>}
      </div>

      {open && results.length > 0 && (
        <FilterChips
          value={filter}
          onChange={setFilter}
          options={[['all', `All (${count('all')})`], ['phrases', `Phrases (${count('phrases')})`], ['words', `Words (${count('words')})`], ['slang', `Slang (${count('slang')})`]]}
        />
      )}

      {!open && <p className="empty">Type in English or Serbian. Accents are optional: “sta” finds “šta”.</p>}
      {open && (
        <div className="card-list">
          {shown.map(({ entry, note }) => <EntryRow key={entry.id} entry={entry} note={note} />)}
          {!results.length && (
            <div className="no-match">
              <strong>No match yet</strong>
              {suggestions.length > 0 && <p>Closest suggestions:</p>}
              {suggestions.map(({ entry, note }) => <EntryRow key={entry.id} entry={entry} note={note} />)}
            </div>
          )}
          {results.length > 0 && !shown.length && <p className="empty pad">Nothing in this filter. Try All.</p>}
        </div>
      )}
    </>
  )
}

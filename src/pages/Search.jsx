import { useMemo, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { search, searchWords } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import EntryRow from '../components/EntryRow.jsx'
import FilterChips from '../components/FilterChips.jsx'
import Icon from '../components/Icons.jsx'
import { useWordCard } from '../components/WordCard.jsx'
import { useWordsReady } from '../lib/words.js'

const isWord = (e) => !/\s/.test(e.serbian.trim())
const isSlang = (e) => e.register === 'slang' || e.register === 'vulgar'
const FILTERS = {
  all: () => true,
  phrases: (e) => !isWord(e),
  words: isWord,
  slang: isSlang,
}

export default function Search() {
  // Query and filter live in the URL, so coming back from an entry restores the same results.
  const [params, setParams] = useSearchParams()
  const query = params.get('q') || ''
  const filter = FILTERS[params.get('f')] ? params.get('f') : 'all'
  const setParam = (key, value, keep) => setParams((p) => { const n = new URLSearchParams(p); value && value !== keep ? n.set(key, value) : n.delete(key); return n }, { replace: true })
  const setQuery = (v) => setParam('q', v)
  const setFilter = (v) => setParam('f', v, 'all')
  // Only pop the keyboard on a fresh search, not when returning to one.
  const [autoFocus] = useState(() => !query)
  const { settings } = useSettings()
  const { results, suggestions } = useMemo(() => search(query, { showVulgar: settings.showVulgar, limit: 60 }), [query, settings.showVulgar])
  const wordsReady = useWordsReady()
  const wordHits = useMemo(() => searchWords(query, { showVulgar: settings.showVulgar }), [query, settings.showVulgar, wordsReady])
  const { open: openWord } = useWordCard()
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
          autoFocus={autoFocus}
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
          options={[['all', `All (${count('all')})`], ['phrases', `Phrases (${count('phrases')})`], ['words', `Single words (${count('words')})`], ['slang', `Slang (${count('slang')})`]]}
        />
      )}

      {!open && <p className="empty">Type in English or Serbian. Accents are optional: “sta” finds “šta”.</p>}
      {open && (
        <div className="card-list">
          {shown.map(({ entry, note }) => <EntryRow key={entry.id} entry={entry} note={note} />)}
          {!results.length && !wordHits.length && (
            <div className="no-match">
              <strong>No match yet</strong>
              {suggestions.length > 0 && <p>Closest suggestions:</p>}
              {suggestions.map(({ entry, note }) => <EntryRow key={entry.id} entry={entry} note={note} />)}
            </div>
          )}
          {!results.length && wordHits.length > 0 && <p className="empty pad">No phrases match, but these words do.</p>}
          {results.length > 0 && !shown.length && <p className="empty pad">Nothing in this filter. Try All.</p>}
        </div>
      )}
      {open && wordHits.length > 0 && (
        <>
          <h2 className="section-label">Word cards</h2>
          <div className="card-list">
            {wordHits.map(({ key, w }) => (
              <div key={key} className="row-wrap">
                <button type="button" className="row word-row" onClick={() => openWord(key)}>
                  <span className="row-en">{w.en}</span>
                  <span className="row-sr">{key}</span>
                  <span className="row-pr">{w.pron}</span>
                </button>
              </div>
            ))}
          </div>
        </>
      )}
    </>
  )
}

import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { bySlug } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import EntryRow from '../components/EntryRow.jsx'
import FilterChips from '../components/FilterChips.jsx'
import Icon from '../components/Icons.jsx'
import { useSettings } from '../lib/settings.jsx'

export default function Category() {
  const { slug } = useParams()
  const cat = bySlug(slug)
  const [sub, setSub] = useState(null)
  const { settings } = useSettings()
  if (!cat) return <p className="empty">Category not found. <Link to="/">Back home</Link></p>

  const inCat = allEntries.filter((e) => e.category === cat.name && (settings.showVulgar || e.register !== 'vulgar'))
  const shown = sub ? inCat.filter((e) => e.subcategory === sub) : inCat

  return (
    <>
      <header className="hero small" style={cat.image ? { backgroundImage: `url(${cat.image})`, backgroundPosition: `center ${cat.focus || '40%'}` } : undefined}>
        <div className="hero-shade" />
        <Link to="/" className="hero-back" aria-label="All categories"><Icon name="chevronL" size={26} /></Link>
        <div className="hero-body">
          <h1>{cat.name}</h1>
          <FilterChips tone="dark" value={sub} onChange={setSub} options={[[null, 'All'], ...cat.subcategories.map((s) => [s, s])]} />
        </div>
      </header>
      <div className="sheet">
        {shown.length ? (
          <div className="list-flat">{shown.map((e) => <EntryRow key={e.id} entry={e} star />)}</div>
        ) : (
          <p className="empty">No entries here yet. This section is coming in a later content batch.</p>
        )}
      </div>
    </>
  )
}

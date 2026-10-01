import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { bySlug } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import EntryRow from '../components/EntryRow.jsx'
import { useSettings } from '../lib/settings.jsx'

export default function Category() {
  const { slug } = useParams()
  const cat = bySlug(slug)
  const [sub, setSub] = useState(null)
  const { settings } = useSettings()
  if (!cat) return <p>Category not found. <Link to="/">Back home</Link></p>

  const inCat = allEntries.filter((e) => e.category === cat.name && (settings.showVulgar || e.register !== 'vulgar'))
  const shown = sub ? inCat.filter((e) => e.subcategory === sub) : inCat

  return (
    <>
      <Link to="/" className="back">← All categories</Link>
      <h1 className="h1">{cat.icon} {cat.name}</h1>
      <div className="chips" role="tablist">
        <button className={`chip ${!sub ? 'on' : ''}`} onClick={() => setSub(null)}>All</button>
        {cat.subcategories.map((s) => (
          <button key={s} className={`chip ${sub === s ? 'on' : ''}`} onClick={() => setSub(s)}>{s}</button>
        ))}
      </div>
      {shown.length ? (
        <div className="list">{shown.map((e) => <EntryRow key={e.id} entry={e} />)}</div>
      ) : (
        <p className="empty">No entries here yet. This section is coming in a later content batch.</p>
      )}
    </>
  )
}

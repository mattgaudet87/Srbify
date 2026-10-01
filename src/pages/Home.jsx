import { Link } from 'react-router-dom'
import { CATEGORIES } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'

export default function Home() {
  const counts = allEntries.reduce((acc, e) => ((acc[e.category] = (acc[e.category] || 0) + 1), acc), {})
  return (
    <>
      <h1 className="h1">Casual Serbian, fast</h1>
      <p className="lede">Search above, or pick a category.</p>
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

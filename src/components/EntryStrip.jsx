import { Link } from 'react-router-dom'

// Horizontal scrolling row of small cards (Favorites / Recently viewed on Home).
export default function EntryStrip({ title, entries }) {
  if (!entries.length) return null
  return (
    <section className="strip">
      <h2>{title}</h2>
      <div className="strip-scroll">
        {entries.map((e) => (
          <Link key={e.id} to={`/entry/${e.id}`} className="mini">
            <span className="row-en">{e.english}</span>
            <span className="mini-sr">{e.serbian}</span>
          </Link>
        ))}
      </div>
    </section>
  )
}

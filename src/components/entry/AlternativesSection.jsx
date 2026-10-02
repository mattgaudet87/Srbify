import { Link } from 'react-router-dom'
import Icon from '../Icons.jsx'
import Sentence from '../Sentence.jsx'
import { entryBySerbian, normalize } from '../../lib/search.js'

export default function AlternativesSection({ e }) {
  return (
    <section>
      <h2>Alternatives</h2>
      <ul className="plain">
        {e.alternatives.map((a, i) => {
          const own = entryBySerbian.get(normalize(a.serbian))
          return (
            <li key={`${i}-${a.serbian}`}>
              <strong><Sentence text={a.serbian} /></strong> <span className="pron-sm inline">{a.pronunciation}</span>
              <div className="muted">{a.nuance}</div>
              {own && own !== e.id && <Link to={`/entry/${own}`} className="alt-link">Open its card<Icon name="chevronR" size={14} /></Link>}
            </li>
          )
        })}
      </ul>
    </section>
  )
}

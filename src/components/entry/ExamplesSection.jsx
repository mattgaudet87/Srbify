import Sentence from '../Sentence.jsx'

export default function ExamplesSection({ e }) {
  return (
    <section>
      <h2>Examples</h2>
      <ul className="plain">
        {e.examples.map((x, i) => (
          <li key={`${i}-${x.serbian}`}>
            {x.context && <span className="ctx">{x.context}</span>}
            <strong><Sentence text={x.serbian} /></strong>
            <span className="pron-sm">{x.pronunciation}</span>
            <div className="muted">{x.english}</div>
          </li>
        ))}
      </ul>
    </section>
  )
}

import Icon from '../Icons.jsx'
import CopyButton from '../CopyButton.jsx'
import Sentence from '../Sentence.jsx'
import { useSettings, isYourForm } from '../../lib/settings.jsx'

const FORM_COLUMNS = [
  ['speaker', 'Speaker'],
  ['describes', 'Describes'],
  ['formal', 'Formality'],
  ['nounGender', 'Noun'],
  ['region', 'Region'],
]

// The "Forms" block of an entry: your own rows up top, then the full table of every form.
export default function FormsSection({ e }) {
  const { settings } = useSettings()
  const yours = e.forms.filter((f) => isYourForm(f, settings))
  const cols = FORM_COLUMNS.filter(([k]) => e.forms.some((f) => f[k]))
  return (
    <section>
      <h2>Forms</h2>
      {yours.length > 0 && (
        <div className="yours-box">
          <div className="yours-title"><Icon name="star" size={14} fill="currentColor" /> Your forms ({settings.speaker === 'male' ? 'a man' : 'a woman'} talking to a {settings.listener === 'female' ? 'woman' : 'man'})</div>
          {yours.map((f, i) => (
            <div key={`${i}-${f.serbian}`} className="yours-line"><strong><Sentence text={f.serbian} /></strong> <span className="pron-sm inline">{f.pronunciation}</span><span className="muted"> · {f.useWhen}</span>
              {f.example && <div className="form-ex"><strong><Sentence text={f.example.serbian} /></strong> <span className="pron-sm inline">{f.example.pronunciation}</span><div className="muted">{f.example.english}</div></div>}
              <span className="yours-copy"><CopyButton text={f.serbian} small /><CopyButton text={f.serbian} plain small label="No accents" /></span></div>
          ))}
        </div>
      )}
      <details className="all-forms" open={yours.length === 0}>
      {yours.length > 0 && <summary>Show all {e.forms.length} forms</summary>}
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Serbian</th>{cols.map(([, l]) => <th key={l}>{l}</th>)}<th>Use when…</th></tr>
          </thead>
          <tbody>
            {e.forms.map((f, i) => (
              <tr key={`${i}-${f.serbian}`} className={isYourForm(f, settings) ? 'yours' : ''}>
                <td>{isYourForm(f, settings) && <Icon name="star" size={13} fill="currentColor" className="star" />}<strong><Sentence text={f.serbian} /></strong><span className="pron-sm">{f.pronunciation}</span></td>
                {cols.map(([k]) => <td key={k}>{f[k] || '—'}</td>)}
                <td>{f.useWhen}{f.example && <div className="form-ex"><strong><Sentence text={f.example.serbian} /></strong><span className="pron-sm">{f.example.pronunciation}</span><div className="muted">{f.example.english}</div></div>}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      </details>
      {e.patternHint && <p className="hint">Pattern: {e.patternHint}</p>}
    </section>
  )
}

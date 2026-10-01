import { Link, useParams } from 'react-router-dom'
import CopyButton from '../components/CopyButton.jsx'
import StarButton from '../components/StarButton.jsx'
import Icon from '../components/Icons.jsx'
import { byName } from '../lib/categories.js'
import { entryById } from '../lib/search.js'
import { useSettings, isYourForm } from '../lib/settings.jsx'
import { RegisterBadge, ChangeBadges, VerifiedBadge } from '../components/Badges.jsx'

const FORM_COLUMNS = [
  ['speaker', 'Speaker'],
  ['describes', 'Describes'],
  ['formal', 'Formality'],
  ['nounGender', 'Noun'],
  ['region', 'Region'],
]

export default function Entry() {
  const { id } = useParams()
  const { settings } = useSettings()
  const e = entryById[id]
  const hiddenVulgar = e?.register === 'vulgar' && !settings.showVulgar
  if (!e) return <p>Entry not found. <Link to="/">Back home</Link></p>
  if (hiddenVulgar) {
    return (
      <>
        <Link to="/" className="back"><Icon name="chevronL" size={26} /></Link>
        <p className="watch">This entry is vulgar and hidden by your settings. <Link to="/settings"><strong>Open Settings</strong></Link> to show vulgar entries.</p>
      </>
    )
  }
  const cat = byName(e.category)
  const yours = (e.forms || []).filter((f) => isYourForm(f, settings))
  const cols = FORM_COLUMNS.filter(([k]) => e.forms?.some((f) => f[k]))

  return (
    <article className="entry">
      <div className="entry-bar">
        <Link to={cat ? `/category/${cat.slug}` : '/'} className="back" aria-label={`Back to ${e.category}`}><Icon name="chevronL" size={26} /></Link>
        <StarButton id={e.id} />
      </div>
      <p className="en-small">{e.english}</p>
      <h1 className="sr-big">{e.serbian}</h1>
      <p className="pron">{e.pronunciation}</p>
      <div className="actions">
        <CopyButton text={e.serbian} />
        <CopyButton text={e.serbian} plain />
      </div>

      <section className="meaning">
        <h2>Meaning</h2>
        <p className="meaning-main">{e.meaning}</p>
        {e.literal && <p className="muted">Literal meaning: {e.literal}</p>}
      </section>

      <div className="badges">
        <RegisterBadge register={e.register} />
        <ChangeBadges entry={e} max={6} />
        <VerifiedBadge verified={e.verified} />
      </div>

      {e.forms?.length > 0 && (
        <section>
          <h2>Forms</h2>
          {yours.length > 0 && (
            <div className="yours-box">
              <div className="yours-title"><Icon name="star" size={14} fill="currentColor" /> Your forms ({settings.speaker === 'male' ? 'a man' : 'a woman'} talking to a {settings.listener === 'female' ? 'woman' : 'man'})</div>
              {yours.map((f) => (
                <div key={f.serbian + f.useWhen} className="yours-line"><strong>{f.serbian}</strong> <span className="pron-sm inline">{f.pronunciation}</span><span className="muted"> · {f.useWhen}</span>
                  {f.example && <div className="form-ex"><strong>{f.example.serbian}</strong> <span className="pron-sm inline">{f.example.pronunciation}</span><div className="muted">{f.example.english}</div></div>}
                  <span className="yours-copy"><CopyButton text={f.serbian} small /><CopyButton text={f.serbian} plain small label="No accents" /></span></div>
              ))}
            </div>
          )}
          <div className="table-wrap">
            <table>
              <thead>
                <tr><th>Serbian</th>{cols.map(([, l]) => <th key={l}>{l}</th>)}<th>Use when…</th></tr>
              </thead>
              <tbody>
                {e.forms.map((f) => (
                  <tr key={f.serbian + f.useWhen} className={isYourForm(f, settings) ? 'yours' : ''}>
                    <td>{isYourForm(f, settings) && <Icon name="star" size={13} fill="currentColor" className="star" />}<strong>{f.serbian}</strong><span className="pron-sm">{f.pronunciation}</span></td>
                    {cols.map(([k]) => <td key={k}>{f[k] || '—'}</td>)}
                    <td>{f.useWhen}{f.example && <div className="form-ex"><strong>{f.example.serbian}</strong><span className="pron-sm">{f.example.pronunciation}</span><div className="muted">{f.example.english}</div></div>}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {e.patternHint && <p className="hint">Pattern: {e.patternHint}</p>}
        </section>
      )}

      {e.alternatives?.length > 0 && (
        <section>
          <h2>Alternatives</h2>
          <ul className="plain">
            {e.alternatives.map((a) => (
              <li key={a.serbian}>
                <strong>{a.serbian}</strong> <span className="pron-sm inline">{a.pronunciation}</span>
                <div className="muted">{a.nuance}</div>
              </li>
            ))}
          </ul>
        </section>
      )}

      {e.examples?.length > 0 && (
        <section>
          <h2>Examples</h2>
          <ul className="plain">
            {e.examples.map((x) => (
              <li key={x.serbian}>
                {x.context && <span className="ctx">{x.context}</span>}
                <strong>{x.serbian}</strong>
                <span className="pron-sm">{x.pronunciation}</span>
                <div className="muted">{x.english}</div>
              </li>
            ))}
          </ul>
        </section>
      )}

      {(e.texting || (e.ijekavian && settings.showIjekavian)) && (
        <section>
          <h2>Texting and regional</h2>
          {e.texting && <p>Texted as: <strong>{e.texting}</strong></p>}
          {e.ijekavian && settings.showIjekavian && <p>Ijekavian: <strong>{e.ijekavian}</strong></p>}
        </section>
      )}

      {e.watchOut && (
        <section className="watch">
          <h2>Watch out</h2>
          <p>{e.watchOut}</p>
        </section>
      )}

      {e.related?.length > 0 && (
        <section>
          <h2>Related</h2>
          <div className="chips">
            {e.related.filter((r) => entryById[r]).map((r) => (
              <Link key={r} to={`/entry/${r}`} className="chip">{entryById[r].serbian}</Link>
            ))}
          </div>
        </section>
      )}
    </article>
  )
}

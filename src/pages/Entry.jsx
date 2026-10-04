import { useEffect } from 'react'
import { Link, useLocation, useNavigate, useParams } from 'react-router-dom'
import { useLibrary } from '../lib/library.jsx'
import { audience } from '../lib/tags.js'
import CopyButton from '../components/CopyButton.jsx'
import SpeakButton from '../components/SpeakButton.jsx'
import FormsSection from '../components/entry/FormsSection.jsx'
import AlternativesSection from '../components/entry/AlternativesSection.jsx'
import ExamplesSection from '../components/entry/ExamplesSection.jsx'
import StarButton from '../components/StarButton.jsx'
import Icon from '../components/Icons.jsx'
import { byName, placementsOf } from '../lib/categories.js'
import { entryById } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import { isVisible } from '../lib/visibility.js'
import { TagPills, ConfidenceBadge } from '../components/Badges.jsx'
import Sentence from '../components/Sentence.jsx'

export default function Entry() {
  const { id } = useParams()
  const { settings } = useSettings()
  const { addRecent } = useLibrary()
  const e = entryById[id]
  const navigate = useNavigate()
  const { key } = useLocation()
  // Back goes to wherever you came from (search results, favorites…); a direct link falls back to the category.
  const goBack = (ev) => { if (key !== 'default') { ev.preventDefault(); navigate(-1) } }
  useEffect(() => { if (e) addRecent(e.id) }, [e, addRecent])
  const hiddenVulgar = e && !isVisible(e, settings)
  if (!e) return <p>Entry not found. <Link to="/">Back home</Link></p>
  if (hiddenVulgar) {
    return (
      <>
        <Link to="/" onClick={goBack} className="back" aria-label="Back"><Icon name="chevronL" size={26} /></Link>
        <p className="watch">This entry is vulgar and hidden by your settings. <Link to="/settings"><strong>Open Settings</strong></Link> to show vulgar entries.</p>
      </>
    )
  }
  const cat = byName(e.category)
  const placements = placementsOf(e)

  return (
    <article className="entry">
      <div className="entry-bar">
        <Link to={cat ? `/category/${cat.slug}` : '/'} onClick={goBack} className="back" aria-label="Back"><Icon name="chevronL" size={26} /></Link>
        <StarButton id={e.id} />
      </div>
      <p className="en-small">{e.english}</p>
      <h1 className="sr-big"><Sentence text={e.serbian} /></h1>
      <p className="pron">{e.pronunciation}</p>
      <div className="actions">
        <SpeakButton text={e.serbian} />
        <CopyButton text={e.serbian} />
        <CopyButton text={e.serbian} plain />
      </div>

      <p className="tap-hint">Tap any Serbian word to see what it means.</p>

      <section className="meaning">
        <h2>Meaning</h2>
        <p className="meaning-main">{e.meaning}</p>
        {e.literal && <p className="muted">Literal meaning: {e.literal}</p>}
      </section>

      <div className="badges">
        <TagPills entry={e} long />
        <ConfidenceBadge entry={e} />
      </div>
      <p className="audience"><strong>Say it to:</strong> {audience(e)}</p>

      {e.forms?.length > 0 && <FormsSection e={e} />}

      {e.alternatives?.length > 0 && <AlternativesSection e={e} />}

      {e.examples?.length > 0 && <ExamplesSection e={e} />}

      {(e.texting || (e.ijekavian && settings.showIjekavian)) && (
        <section>
          <h2>Texting and regional</h2>
          {e.texting && <p>Texted as: <strong>{e.texting}</strong></p>}
          {e.ijekavian && settings.showIjekavian && <p>Ijekavian: <strong><Sentence text={e.ijekavian} /></strong></p>}
        </section>
      )}

      {e.watchOut && (
        <section className="watch">
          <h2>Watch out</h2>
          <p>{e.watchOut}</p>
        </section>
      )}

      {placements.length > 0 && (
        <section>
          <h2>Find it under</h2>
          <div className="also-in">
            {placements.map((pl) => {
              const c = byName(pl.category)
              return c && <Link key={pl.category + pl.subcategory} to={`/category/${c.slug}?sub=${encodeURIComponent(pl.subcategory)}`}>{pl.subcategory} <small>· {pl.category}</small></Link>
            })}
          </div>
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

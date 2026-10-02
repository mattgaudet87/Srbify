import { useMemo, useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { useLibrary } from '../lib/library.jsx'
import { useSettings } from '../lib/settings.jsx'
import { allEntries, entryById } from '../lib/search.js'
import { bySlug, placementsOf } from '../lib/categories.js'
import { isVisible } from '../lib/visibility.js'
import Sentence from '../components/Sentence.jsx'

const shuffle = (a) => { const b = [...a]; for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [b[i], b[j]] = [b[j], b[i]] } return b }

// Flashcards: see the English, say it, flip to check. "Again" puts a card back in the pile.
// With ?cat=…&sub=… it drills one topic; otherwise it drills your favorites.
export default function Review() {
  const { favorites } = useLibrary()
  const { settings } = useSettings()
  const [params] = useSearchParams()
  const cat = bySlug(params.get('cat'))
  const sub = cat?.subcategories.includes(params.get('sub')) ? params.get('sub') : null
  const topic = cat && sub ? { cat, sub } : null
  const ids = useMemo(() => {
    if (topic) return allEntries.filter((e) => isVisible(e, settings) && placementsOf(e).some((p) => p.category === topic.cat.name && p.subcategory === topic.sub)).map((e) => e.id)
    return favorites.filter((id) => entryById[id] && isVisible(entryById[id], settings))
  }, [topic?.cat.slug, topic?.sub, favorites, settings.showVulgar])
  return <Practice key={topic ? `${topic.cat.slug}/${topic.sub}` : 'favorites'} ids={ids} topic={topic} />
}

function Practice({ ids, topic }) {
  const start = useMemo(() => shuffle(ids), [ids])
  const [queue, setQueue] = useState(start)
  const [shown, setShown] = useState(false)
  const [done, setDone] = useState(0)
  const e = entryById[queue[0]]
  const total = start.length
  const backTo = topic ? `/category/${topic.cat.slug}?sub=${encodeURIComponent(topic.sub)}` : '/favorites'

  const next = (again) => {
    setQueue((q) => (again ? [...q.slice(1), q[0]] : q.slice(1)))
    if (!again) setDone((n) => n + 1)
    setShown(false)
  }

  return (
    <>
      <h1 className="title">Practice</h1>
      {topic && <p className="muted">{topic.sub} · {topic.cat.name}</p>}
      {!total ? (
        <p className="empty">{topic ? 'Nothing to practice in this topic yet.' : 'Star a few phrases first, then come back to practice them.'} <Link to="/search">Find a phrase</Link></p>
      ) : !e ? (
        <div className="review-card">
          <div className="review-en">Done! You went through {done} {done === 1 ? 'phrase' : 'phrases'}.</div>
          <div className="review-actions">
            <button type="button" className="btn" onClick={() => { setQueue(shuffle(start)); setDone(0) }}>Go again</button>
            <Link to={backTo} className="btn ghost">Back</Link>
          </div>
        </div>
      ) : (
        <>
          <div className="review-card">
            <div className="review-en">{e.english}</div>
            {shown ? (
              <>
                <div className="review-sr"><Sentence text={e.serbian} /></div>
                <div className="review-pr">{e.pronunciation}</div>
                <Link to={`/entry/${e.id}`} className="muted">Open full entry</Link>
              </>
            ) : <div className="muted">Say it out loud, then check.</div>}
            <div className="review-actions">
              {shown ? (
                <>
                  <button type="button" className="btn ghost" onClick={() => next(true)}>Again</button>
                  <button type="button" className="btn" onClick={() => next(false)}>Got it</button>
                </>
              ) : <button type="button" className="btn" onClick={() => setShown(true)}>Show answer</button>}
            </div>
          </div>
          <p className="review-count">{done} of {total} done · {queue.length} left</p>
        </>
      )}
    </>
  )
}

import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLibrary } from '../lib/library.jsx'
import { useSettings } from '../lib/settings.jsx'
import { entryById } from '../lib/search.js'
import Sentence from '../components/Sentence.jsx'

const shuffle = (a) => { const b = [...a]; for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [b[i], b[j]] = [b[j], b[i]] } return b }

// Flashcards from your favorites: see the English, say it, flip to check. "Again" puts a card back in the pile.
export default function Review() {
  const { favorites } = useLibrary()
  const { settings } = useSettings()
  const start = useMemo(() => shuffle(favorites.filter((id) => entryById[id] && (settings.showVulgar || entryById[id].register !== 'vulgar'))), [favorites, settings.showVulgar])
  const [queue, setQueue] = useState(start)
  const [shown, setShown] = useState(false)
  const [done, setDone] = useState(0)
  const e = entryById[queue[0]]

  const next = (again) => {
    setQueue((q) => (again ? [...q.slice(1), q[0]] : q.slice(1)))
    if (!again) setDone((n) => n + 1)
    setShown(false)
  }

  return (
    <>
      <h1 className="title">Practice</h1>
      {!start.length ? (
        <p className="empty">Star a few phrases first, then come back to practice them. <Link to="/search">Find a phrase</Link></p>
      ) : !e ? (
        <div className="review-card">
          <div className="review-en">Done! You went through {done} {done === 1 ? 'phrase' : 'phrases'}.</div>
          <div className="review-actions">
            <button type="button" className="btn" onClick={() => { setQueue(shuffle(start)); setDone(0) }}>Go again</button>
            <Link to="/favorites" className="btn ghost">Back</Link>
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
          <p className="review-count">{queue.length} left</p>
        </>
      )}
    </>
  )
}

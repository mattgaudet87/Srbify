import { useState } from 'react'
import { Link } from 'react-router-dom'
import { CATEGORIES } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import Icon from '../components/Icons.jsx'

// The grammar tip shows for the first 3 visits (one visit = one browser session) unless closed sooner.
const TIP_VISITS = 3
function useGrammarTip() {
  const [show, setShow] = useState(() => {
    try {
      if (localStorage.getItem('srbify.grammarTip.closed')) return false
      let n = Number(localStorage.getItem('srbify.grammarTip.visits') || 0)
      if (!sessionStorage.getItem('srbify.grammarTip.counted')) {
        n += 1
        localStorage.setItem('srbify.grammarTip.visits', String(n))
        sessionStorage.setItem('srbify.grammarTip.counted', '1')
      }
      return n <= TIP_VISITS
    } catch {
      return true
    }
  })
  const close = () => {
    setShow(false)
    try { localStorage.setItem('srbify.grammarTip.closed', '1') } catch { /* private mode */ }
  }
  return [show, close]
}

export default function Home() {
  const [showTip, closeTip] = useGrammarTip()
  const { settings } = useSettings()
  const visible = allEntries.filter((e) => settings.showVulgar || e.register !== 'vulgar')
  const hidden = allEntries.length - visible.length

  return (
    <>
      <header className="hero">
        <div className="hero-shade" />
        <Link to="/settings" className="hero-gear" aria-label="Settings"><Icon name="settings" size={24} /></Link>
        <div className="hero-body">
          <div className="brand-row">
            <img className="brand-tile" src="/logo-icon.png" alt="" width="52" height="52" />
            <h1>Srbify</h1>
          </div>
          <p>Casual Serbian, made easy for texting.</p>
          <Link to="/search" className="hero-search">
            <Icon name="search" size={22} />
            <span>Search English or Serbian…</span>
          </Link>
        </div>
      </header>

      <div className="sheet">
        <div className="sheet-head">
          <h2>Categories</h2>
        </div>
        {hidden > 0 && <p className="hint">{hidden} vulgar {hidden === 1 ? 'entry is' : 'entries are'} hidden. <Link to="/settings">Change in Settings</Link></p>}
        <div className="grid">
          {CATEGORIES.map((c) => (
            <Link key={c.slug} to={`/category/${c.slug}`} className="tile">
              <Icon name={c.icon} size={28} />
              <span className="tile-name">{c.name}</span>
              <span className="tile-blurb">{c.blurb}</span>
            </Link>
          ))}
        </div>
        {showTip && <div className="grammar-card">
          <button className="grammar-close" aria-label="Close tip" onClick={closeTip}><Icon name="x" size={16} strokeWidth={2.4} /></button>
          <strong>Looking for grammar?</strong>
          <span className="muted">Verbs and Basics are laid out the way a textbook would.</span>
          <div className="grammar-links">
            {CATEGORIES.filter((c) => c.grammar).map((c) => <Link key={c.slug} to={`/category/${c.slug}`}>{c.name}</Link>)}
          </div>
        </div>}
      </div>
    </>
  )
}

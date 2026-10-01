import { Link } from 'react-router-dom'
import { CATEGORIES } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import { useSettings } from '../lib/settings.jsx'
import Icon from '../components/Icons.jsx'

export default function Home() {
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
            </Link>
          ))}
        </div>
      </div>
    </>
  )
}

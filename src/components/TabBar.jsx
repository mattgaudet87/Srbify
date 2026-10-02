import { NavLink, useLocation } from 'react-router-dom'
import Icon from './Icons.jsx'

const TABS = [
  { to: '/', label: 'Home', icon: 'home' },
  { to: '/search', label: 'Search', icon: 'search' },
  { to: '/favorites', label: 'Favorites', icon: 'star' },
  { to: '/settings', label: 'Settings', icon: 'settings' },
]

export default function TabBar() {
  const { pathname } = useLocation()
  // Categories and entries live under the Home tab.
  const isHome = !['/search', '/favorites', '/review', '/settings'].some((p) => pathname.startsWith(p))
  return (
    <nav className="tabbar" aria-label="Main">
      <div className="tabbar-inner">
        {TABS.map((t) => {
          const active = t.to === '/' ? isHome : pathname.startsWith(t.to) || (t.to === '/favorites' && pathname.startsWith('/review'))
          return (
            <NavLink key={t.to} to={t.to} className={`tab ${active ? 'on' : ''}`} aria-current={active ? 'page' : undefined}>
              <Icon name={t.icon} size={24} fill={active && t.icon !== 'search' ? 'currentColor' : 'none'} />
              <span>{t.label}</span>
            </NavLink>
          )
        })}
      </div>
    </nav>
  )
}

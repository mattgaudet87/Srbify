import { lazy, Suspense, useEffect } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import TabBar from './components/TabBar.jsx'
import Home from './pages/Home.jsx'
import Search from './pages/Search.jsx'
import Favorites from './pages/Favorites.jsx'
import Category from './pages/Category.jsx'
import Entry from './pages/Entry.jsx'
import Settings from './pages/Settings.jsx'
import NotFound from './pages/NotFound.jsx'

// Rarely-opened pages load on demand.
const Review = lazy(() => import('./pages/Review.jsx'))
const Checks = lazy(() => import('./pages/Checks.jsx'))

export default function App() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [pathname])

  return (
    <div className="app">
      <main className="page">
        <Suspense fallback={null}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<Search />} />
          <Route path="/favorites" element={<Favorites />} />
          <Route path="/category/:slug" element={<Category />} />
          <Route path="/entry/:id" element={<Entry />} />
          <Route path="/review" element={<Review />} />
          <Route path="/checks" element={<Checks />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        </Suspense>
      </main>
      <TabBar />
    </div>
  )
}

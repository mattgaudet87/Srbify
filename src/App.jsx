import { useEffect } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import SearchBar from './components/SearchBar.jsx'
import Home from './pages/Home.jsx'
import Category from './pages/Category.jsx'
import Entry from './pages/Entry.jsx'

export default function App() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [pathname])

  return (
    <div className="app">
      <SearchBar />
      <main className="page">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/category/:slug" element={<Category />} />
          <Route path="/entry/:id" element={<Entry />} />
          <Route path="*" element={<Home />} />
        </Routes>
      </main>
    </div>
  )
}

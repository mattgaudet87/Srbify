import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'

// Favorites and recently viewed entries, kept in the browser (localStorage).
const KEY = 'srbify-library'
const MAX_RECENT = 8

const LibraryContext = createContext(null)

function load() {
  try {
    const d = JSON.parse(localStorage.getItem(KEY) || '{}')
    return { favorites: d.favorites || [], recent: d.recent || [] }
  } catch {
    return { favorites: [], recent: [] }
  }
}

export function LibraryProvider({ children }) {
  const [lib, setLib] = useState(load)

  useEffect(() => {
    try {
      localStorage.setItem(KEY, JSON.stringify(lib))
    } catch {
      // storage unavailable: nothing persists, app still works
    }
  }, [lib])

  // Another tab or the installed app changed favorites: pick up their version instead of overwriting it later.
  useEffect(() => {
    const onStorage = (ev) => { if (ev.key === KEY) setLib(load()) }
    window.addEventListener('storage', onStorage)
    return () => window.removeEventListener('storage', onStorage)
  }, [])

  const toggleFavorite = useCallback((id) => {
    setLib((l) => ({ ...l, favorites: l.favorites.includes(id) ? l.favorites.filter((f) => f !== id) : [id, ...l.favorites] }))
  }, [])
  const setFavorites = useCallback((favorites) => setLib((l) => ({ ...l, favorites })), [])
  const addRecent = useCallback((id) => {
    setLib((l) => (l.recent[0] === id ? l : { ...l, recent: [id, ...l.recent.filter((r) => r !== id)].slice(0, MAX_RECENT) }))
  }, [])

  const value = useMemo(() => ({ ...lib, toggleFavorite, setFavorites, addRecent }), [lib, toggleFavorite, setFavorites, addRecent])
  return <LibraryContext.Provider value={value}>{children}</LibraryContext.Provider>
}

export const useLibrary = () => useContext(LibraryContext)

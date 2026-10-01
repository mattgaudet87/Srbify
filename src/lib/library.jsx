import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'

// Favorites, kept in the browser (localStorage).
const KEY = 'srbify-library'

const LibraryContext = createContext(null)

function load() {
  try {
    const d = JSON.parse(localStorage.getItem(KEY) || '{}')
    return { favorites: d.favorites || [] }
  } catch {
    return { favorites: [] }
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

  const toggleFavorite = useCallback((id) => {
    setLib((l) => ({ ...l, favorites: l.favorites.includes(id) ? l.favorites.filter((f) => f !== id) : [id, ...l.favorites] }))
  }, [])

  const value = useMemo(() => ({ ...lib, toggleFavorite }), [lib, toggleFavorite])
  return <LibraryContext.Provider value={value}>{children}</LibraryContext.Provider>
}

export const useLibrary = () => useContext(LibraryContext)

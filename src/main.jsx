import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import { SettingsProvider } from './lib/settings.jsx'
import { LibraryProvider } from './lib/library.jsx'
import { WordProvider } from './components/WordCard.jsx'
import { loadWords } from './lib/words.js'
import './styles.css'

loadWords()
// Fetch the lazy pages when the browser is idle so they also work offline.
if (import.meta.env.PROD) window.addEventListener('load', () => (window.requestIdleCallback || setTimeout)(() => { import('./pages/Review.jsx'); import('./pages/Checks.jsx') }))

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <SettingsProvider>
        <LibraryProvider>
          <WordProvider>
            <App />
          </WordProvider>
        </LibraryProvider>
      </SettingsProvider>
    </BrowserRouter>
  </React.StrictMode>
)

// Offline support: only register in the production build.
if ('serviceWorker' in navigator && import.meta.env.PROD) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(() => {})
  })
}

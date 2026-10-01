import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import { SettingsProvider } from './lib/settings.jsx'
import { LibraryProvider } from './lib/library.jsx'
import './styles.css'

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <SettingsProvider>
        <LibraryProvider>
          <App />
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

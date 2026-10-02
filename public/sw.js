// Srbify service worker: makes the app installable and work offline.
// Strategy: pre-cache the app shell; for everything else on this site, answer from cache
// and refresh the cache in the background (so updates arrive on the next visit).
const CACHE = 'srbify-v3'
const SHELL = ['/', '/index.html', '/manifest.webmanifest', '/favicon.png', '/logo-192.png', '/logo-512.png', '/apple-touch-icon.png', '/wordmark.png']

// Category and header photos, so every screen looks right offline. Cached best-effort: one miss never blocks install.
const PHOTOS = [
  'header-belgrade-river', 'cafe-street-sunset', 'friends-picnic-sunset', 'couple-sunset', 'backpack-map-bridge', 'sign-putovanja-map',
  'train-platform-backpack', 'camera-map-fortress', 'victor-monument-sunset', 'cevapi-table',
].map((n) => `/images/${n}.jpg`)

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(SHELL).then(() => Promise.allSettled(PHOTOS.map((u) => c.add(u)))))
      .then(() => self.skipWaiting())
  )
})

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  )
})

self.addEventListener('fetch', (event) => {
  const req = event.request
  const url = new URL(req.url)
  if (req.method !== 'GET' || url.origin !== self.location.origin) return

  // Page loads: try the network, fall back to the cached app shell (client-side routing handles the URL).
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone()
          caches.open(CACHE).then((c) => c.put('/index.html', copy))
          return res
        })
        .catch(() => caches.match('/index.html'))
    )
    return
  }

  // Assets: cache first, refresh in the background.
  event.respondWith(
    caches.match(req).then((cached) => {
      const network = fetch(req)
        .then((res) => {
          if (res.ok) {
            const copy = res.clone()
            caches.open(CACHE).then((c) => c.put(req, copy))
          }
          return res
        })
        .catch(() => cached)
      return cached || network
    })
  )
})

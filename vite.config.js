import { readFileSync, writeFileSync } from 'node:fs'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const pkg = JSON.parse(readFileSync('./package.json', 'utf8'))

// Stamp the service worker's cache name with the build time so every deploy drops the old cache.
const stampServiceWorker = () => ({
  name: 'stamp-sw',
  apply: 'build',
  closeBundle() {
    const file = 'dist/sw.js'
    try { writeFileSync(file, readFileSync(file, 'utf8').replace(/srbify-v\d+/, `srbify-${Date.now()}`)) } catch { /* no sw in this build */ }
  },
})

export default defineConfig({
  plugins: [react(), stampServiceWorker()],
  define: { __APP_VERSION__: JSON.stringify(pkg.version) },
})

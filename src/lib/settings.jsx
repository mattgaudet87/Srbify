import { createContext, useContext, useEffect, useMemo, useState } from 'react'

const KEY = 'srbify-settings'
const DEFAULTS = { speaker: 'male', listener: 'female', showVulgar: false, showIjekavian: true, theme: 'system' }

const SettingsContext = createContext(null)

function load() {
  try {
    return { ...DEFAULTS, ...JSON.parse(localStorage.getItem(KEY) || '{}') }
  } catch {
    return DEFAULTS
  }
}

export function SettingsProvider({ children }) {
  const [settings, setSettings] = useState(load)

  useEffect(() => {
    try {
      localStorage.setItem(KEY, JSON.stringify(settings))
    } catch {
      // storage unavailable (private mode): settings just won't persist
    }
  }, [settings])

  // 'system' leaves the attribute off so the OS preference (prefers-color-scheme) decides.
  useEffect(() => {
    const root = document.documentElement
    if (settings.theme === 'system') root.removeAttribute('data-theme')
    else root.setAttribute('data-theme', settings.theme)
  }, [settings.theme])

  const value = useMemo(() => ({ settings, update: (patch) => setSettings((s) => ({ ...s, ...patch })) }), [settings])
  return <SettingsContext.Provider value={value}>{children}</SettingsContext.Provider>
}

export const useSettings = () => useContext(SettingsContext)

// Is this row of an entry's forms table "your form" under the current settings?
// A row counts if every tag it carries matches: the speaker, who you're talking to,
// casual (not polite) and Serbian (ekavian) spelling. Noun gender never highlights.
export function isYourForm(form, { speaker, listener }) {
  const tags = [form.speaker, form.describes, form.formal, form.region].filter(Boolean)
  if (!tags.length) return false
  if (form.speaker && form.speaker !== speaker) return false
  if (form.describes) {
    const wanted = listener === 'female' ? 'her' : 'him'
    if (form.describes !== wanted) return false
  }
  if (form.formal && form.formal !== 'casual') return false
  if (form.region && form.region !== 'serbia') return false
  return true
}

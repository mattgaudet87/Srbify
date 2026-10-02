import { useSettings } from '../lib/settings.jsx'
import Icon from '../components/Icons.jsx'
import CopyButton from '../components/CopyButton.jsx'
import { allEntries } from '../lib/search.js'

const unverified = allEntries.filter((e) => !e.verified)
// A plain list a Serbian speaker can mark up: English, Serbian, and the entry id to change in entries.json.
const CHECK_LIST = unverified.map((e) => `${e.english} = ${e.serbian}  [${e.id}]`).join('\n')

function Segment({ label, value, options, onChange }) {
  return (
    <div className="set-row">
      <div className="set-label" id={`l-${label}`}>{label}</div>
      <div className="seg" role="radiogroup" aria-labelledby={`l-${label}`}>
        {options.map(([v, text]) => (
          <button key={v} role="radio" aria-checked={value === v} className={value === v ? 'on' : ''} onClick={() => onChange(v)}>{text}</button>
        ))}
      </div>
    </div>
  )
}

function Toggle({ label, desc, on, onChange }) {
  return (
    <div className="set-row toggle-row">
      <div>
        <div className="set-label">{label}</div>
        <div className="set-desc">{desc}</div>
      </div>
      <button role="switch" aria-checked={on} aria-label={label} className={`switch ${on ? 'on' : ''}`} onClick={() => onChange(!on)}><span /></button>
    </div>
  )
}

const THEMES = [['light', 'Light mode', 'sun'], ['dark', 'Dark mode', 'moon'], ['system', 'Use system setting', 'monitor']]

export default function Settings() {
  const { settings, update } = useSettings()
  return (
    <>
      <h1 className="title">Settings</h1>

      <h2 className="group-title">Your perspective</h2>
      <div className="set-card">
        <Segment label="I am" value={settings.speaker} options={[['male', 'Male'], ['female', 'Female']]} onChange={(v) => update({ speaker: v })} />
        <Segment label="Usually talking to" value={settings.listener} options={[['female', 'Female'], ['male', 'Male']]} onChange={(v) => update({ listener: v })} />
      </div>
      <p className="hint">This decides which row in a forms table is highlighted as yours (e.g. how a man talks about himself, and how to address a woman).</p>

      <h2 className="group-title">Content</h2>
      <div className="set-card">
        <Toggle label="Show vulgar entries" desc="Display slang and strongly vulgar words. Off hides them everywhere, including search." on={settings.showVulgar} onChange={(v) => update({ showVulgar: v })} />
        <Toggle label="Show ijekavian notes" desc="Ijekavian forms (e.g. lijepo, gdje) when it differs from the main ekavian form." on={settings.showIjekavian} onChange={(v) => update({ showIjekavian: v })} />
      </div>

      <h2 className="group-title">Appearance</h2>
      <div className="set-card" role="radiogroup" aria-label="Appearance">
        {THEMES.map(([v, text, icon]) => (
          <button key={v} role="radio" aria-checked={settings.theme === v} className={`theme-row ${settings.theme === v ? 'on' : ''}`} onClick={() => update({ theme: v })}>
            <Icon name={icon} size={20} />
            <span>{text}</span>
            {settings.theme === v && <Icon name="check" size={20} className="theme-check" />}
          </button>
        ))}
      </div>

      <h2 className="group-title">Checking</h2>
      <div className="set-card">
        <div className="about">
          <span className="set-desc">{unverified.length} of {allEntries.length} entries haven’t been checked by a native speaker yet.</span>
          <CopyButton text={CHECK_LIST} small label="Copy the list to send for checking" />
        </div>
      </div>

      <h2 className="group-title">About</h2>
      <div className="set-card">
        <div className="about">
          <img src="/wordmark.png" alt="Srbify" width="150" />
          <span className="set-desc">Version {__APP_VERSION__} · Saved in this browser only</span>
        </div>
      </div>
    </>
  )
}

import { Link } from 'react-router-dom'
import { useSettings } from '../lib/settings.jsx'

function Choice({ label, value, options, onChange }) {
  return (
    <div className="setting">
      <div className="setting-label">{label}</div>
      <div className="seg" role="radiogroup" aria-label={label}>
        {options.map(([v, text]) => (
          <button key={v} role="radio" aria-checked={value === v} className={value === v ? 'on' : ''} onClick={() => onChange(v)}>{text}</button>
        ))}
      </div>
    </div>
  )
}

export default function Settings() {
  const { settings, update } = useSettings()
  const onOff = [[true, 'On'], [false, 'Off']]
  return (
    <>
      <Link to="/" className="back">← Home</Link>
      <h1 className="h1">Settings</h1>
      <p className="lede">Saved in this browser only.</p>

      <Choice label="I am" value={settings.speaker} options={[['male', 'Male'], ['female', 'Female']]} onChange={(v) => update({ speaker: v })} />
      <Choice label="Usually talking to" value={settings.listener} options={[['female', 'Female'], ['male', 'Male']]} onChange={(v) => update({ listener: v })} />
      <p className="hint">These decide which rows in a forms table are highlighted as “your form”.</p>

      <Choice label="Show vulgar entries" value={settings.showVulgar} options={onOff} onChange={(v) => update({ showVulgar: v })} />
      <p className="hint">Off hides vulgar entries everywhere, including search, so you never send a swear by accident.</p>

      <Choice label="Show ijekavian notes" value={settings.showIjekavian} options={onOff} onChange={(v) => update({ showIjekavian: v })} />
      <p className="hint">Ijekavian (lijepo, gdje) is the Bosnian, Montenegrin and Croatian spelling. Shown as a note so you recognise it.</p>
    </>
  )
}

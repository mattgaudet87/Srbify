export default function FilterChips({ options, value, onChange, tone = 'light' }) {
  return (
    <div className={`chips ${tone}`} role="tablist">
      {options.map(([v, label]) => (
        <button key={String(v)} role="tab" aria-selected={value === v} className={`chip ${value === v ? 'on' : ''}`} onClick={() => onChange(v)}>{label}</button>
      ))}
    </div>
  )
}

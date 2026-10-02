import { NUMBERS, BIG_NUMBERS } from '../lib/numbers.js'

const fmt = (n) => n.toLocaleString('en-US')

// Full number-by-number table, 1 to 100 then the big round numbers.
export default function NumbersTable() {
  return (
    <section className="numbers">
      <div className="sub-head"><h2>Numbers, one by one</h2><span>1 to 100</span></div>
      <div className="table-wrap">
        <table className="num-table">
          <thead><tr><th>Number</th><th>Serbian</th><th>Say it</th></tr></thead>
          <tbody>
            {NUMBERS.map(([n, sr, pr]) => (
              <tr key={n}><td className="num">{n}</td><td><strong>{sr}</strong></td><td><span className="pron-sm">{pr}</span></td></tr>
            ))}
            {BIG_NUMBERS.map(([n, sr, pr, note]) => (
              <tr key={n} className="num-big"><td className="num">{fmt(n)}</td><td><strong>{sr}</strong>{note && <div className="muted">{note}</div>}</td><td><span className="pron-sm">{pr}</span></td></tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="hint">Above 20, say the tens first, then the ones: <strong>dvadeset jedan</strong> (21). Only 1 and 2 change with the noun, see below.</p>
    </section>
  )
}

import { useMemo, useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { bySlug, placementsOf } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import { entryTags, tagFilterLabel } from '../lib/tags.js'
import EntryRow from '../components/EntryRow.jsx'
import FilterChips from '../components/FilterChips.jsx'
import Icon from '../components/Icons.jsx'
import { useSettings } from '../lib/settings.jsx'

const TAG_ORDER = ['casual', 'neutral', 'formal', 'flirty', 'slang', 'vulgar', 'texting', 'past', 'present', 'future', 'mf-speaker', 'mf-about', 'noun-gender', 'plural', 'never']

export default function Category() {
  const { slug } = useParams()
  const cat = bySlug(slug)
  const [params, setParams] = useSearchParams()
  const sub = params.get('sub')
  const [tag, setTag] = useState(null)
  const { settings } = useSettings()

  // Each entry paired with its subcategory placements in this category (an entry can sit in several).
  const inCat = useMemo(() => cat ? allEntries
    .filter((e) => settings.showVulgar || e.register !== 'vulgar')
    .map((e) => ({ e, subs: placementsOf(e).filter((p) => p.category === cat.name).map((p) => p.subcategory) }))
    .filter((x) => x.subs.length) : [], [cat, settings.showVulgar])
  const tagKeys = useMemo(() => new Set(inCat.filter((x) => !sub || x.subs.includes(sub)).flatMap(({ e }) => entryTags(e).map((t) => t.key))), [inCat, sub])

  if (!cat) return <p className="empty">Category not found. <Link to="/">Back home</Link></p>

  const setSub = (s) => { setTag(null); setParams(s ? { sub: s } : {}, { replace: true }) }
  const pass = ({ e }) => !tag || entryTags(e).some((t) => t.key === tag)
  const countIn = (s) => inCat.filter((x) => x.subs.includes(s)).length
  const visibleSubs = cat.subcategories.filter((s) => (sub ? s === sub : true))
  const groups = visibleSubs.map((s) => [s, inCat.filter((x) => x.subs.includes(s)).filter(pass)]).filter(([, l]) => l.length)
  const empty = cat.subcategories.filter((s) => !countIn(s))
  const tagOptions = TAG_ORDER.filter((k) => tagKeys.has(k))

  return (
    <>
      <header className="hero small" style={cat.image ? { backgroundImage: `url(${cat.image})`, backgroundPosition: `center ${cat.focus || '40%'}` } : undefined}>
        <div className="hero-shade" />
        <Link to="/" className="hero-back" aria-label="All categories"><Icon name="chevronL" size={26} /></Link>
        <div className="hero-body">
          <h1>{cat.name}</h1>
          <FilterChips tone="dark" value={sub} onChange={setSub} options={[[null, 'All'], ...cat.subcategories.filter((s) => countIn(s)).map((s) => [s, s])]} />
        </div>
      </header>
      <div className="sheet">
        {tagOptions.length > 1 && (
          <div className="filter-row" role="tablist" aria-label="Filter by tag">
            <span className="lbl">Tags</span>
            <button role="tab" aria-selected={!tag} className={`chip tagchip ${!tag ? 'on' : ''}`} onClick={() => setTag(null)}>Any</button>
            {tagOptions.map((k) => <button key={k} role="tab" aria-selected={tag === k} className={`chip tagchip ${tag === k ? 'on' : ''}`} onClick={() => setTag(tag === k ? null : k)}>{tagFilterLabel[k]}</button>)}
          </div>
        )}
        {groups.length ? groups.map(([s, list]) => (
          <section key={s}>
            {!sub && <div className="sub-head"><h2>{s}</h2><span>{list.length}</span></div>}
            <div className="list-flat">{list.map(({ e }) => <EntryRow key={e.id} entry={e} star />)}</div>
          </section>
        )) : (
          <p className="empty">{inCat.length ? 'Nothing matches that tag here. Try Any.' : 'No entries here yet. This section is coming in a later content batch.'}</p>
        )}
        {!sub && !tag && empty.length > 0 && inCat.length > 0 && <p className="coming">Coming soon: {empty.join(' · ')}</p>}
      </div>
    </>
  )
}

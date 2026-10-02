import { useEffect, useMemo, useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { bySlug, placementsOf } from '../lib/categories.js'
import { allEntries } from '../lib/search.js'
import { entryTags, tagFilterLabel } from '../lib/tags.js'
import EntryRow from '../components/EntryRow.jsx'
import Icon from '../components/Icons.jsx'
import NumbersTable from '../components/NumbersTable.jsx'
import { useSettings } from '../lib/settings.jsx'

const TAG_ORDER = ['casual', 'neutral', 'formal', 'flirty', 'slang', 'vulgar', 'texting', 'past', 'present', 'future', 'mf-speaker', 'mf-about', 'noun-gender', 'plural', 'never']

export default function Category() {
  const { slug } = useParams()
  const cat = bySlug(slug)
  const [params, setParams] = useSearchParams()
  const sub = params.get('sub')
  const [tag, setTag] = useState(null)
  const { settings } = useSettings()
  useEffect(() => { setTag(null) }, [sub])

  // Each entry paired with its subcategory placements in this category (an entry can sit in several).
  const inCat = useMemo(() => cat ? allEntries
    .filter((e) => settings.showVulgar || e.register !== 'vulgar')
    .map((e) => ({ e, subs: placementsOf(e).filter((p) => p.category === cat.name).map((p) => p.subcategory) }))
    .filter((x) => x.subs.length) : [], [cat, settings.showVulgar])
  const tagKeys = useMemo(() => new Set(inCat.filter((x) => !sub || x.subs.includes(sub)).flatMap(({ e }) => entryTags(e).map((t) => t.key))), [inCat, sub])

  if (!cat) return <p className="empty">Category not found. <Link to="/">Back home</Link></p>

  const subOk = cat.subcategories.includes(sub)
  const pass = ({ e }) => !tag || entryTags(e).some((t) => t.key === tag)
  const countIn = (s) => inCat.filter((x) => x.subs.includes(s)).length
  const list = subOk ? inCat.filter((x) => x.subs.includes(sub)).filter(pass) : []
  const tagOptions = TAG_ORDER.filter((k) => tagKeys.has(k))
  const heroStyle = cat.image ? { backgroundImage: `url(${cat.image})`, backgroundPosition: `center ${cat.focus || '40%'}` } : undefined

  return (
    <>
      <header className="hero small" style={heroStyle}>
        <div className="hero-shade" />
        <Link to={subOk ? `/category/${cat.slug}` : '/'} className="hero-back" aria-label={subOk ? cat.name : 'All categories'}><Icon name="chevronL" size={26} /></Link>
        <div className="hero-body">
          {subOk && <p className="crumb">{cat.name}</p>}
          <h1>{subOk ? sub : cat.name}</h1>
        </div>
      </header>
      <div className="sheet">
        {!subOk ? (
          <>
            <div className="sheet-head"><h2>Pick a topic</h2></div>
            <div className="grid sub-grid">
              {cat.subcategories.map((s) => {
                const n = countIn(s)
                return n ? (
                  <Link key={s} to={`/category/${cat.slug}?sub=${encodeURIComponent(s)}`} className="tile">
                    <span className="tile-name">{s}</span>
                    <span className="tile-blurb">{n} {n === 1 ? 'entry' : 'entries'}</span>
                  </Link>
                ) : (
                  <div key={s} className="tile tile-soon" aria-disabled="true">
                    <span className="tile-name">{s}</span>
                    <span className="tile-blurb">Coming soon</span>
                  </div>
                )
              })}
            </div>
          </>
        ) : (
          <>
            {cat.slug === 'basics' && sub === 'Numbers' && <NumbersTable />}
            {tagOptions.length > 1 && (
              <div className="filter-row" role="tablist" aria-label="Filter by tag">
                <span className="lbl">Tags</span>
                <button role="tab" aria-selected={!tag} className={`chip tagchip ${!tag ? 'on' : ''}`} onClick={() => setTag(null)}>Any</button>
                {tagOptions.map((k) => <button key={k} role="tab" aria-selected={tag === k} className={`chip tagchip ${tag === k ? 'on' : ''}`} onClick={() => setTag(tag === k ? null : k)}>{tagFilterLabel[k]}</button>)}
              </div>
            )}
            {list.length ? (
              <div className="list-flat">{list.map(({ e }) => <EntryRow key={e.id} entry={e} star />)}</div>
            ) : (
              <p className="empty">{countIn(sub) ? 'Nothing matches that tag here. Try Any.' : 'No entries here yet. This section is coming in a later content batch.'}</p>
            )}
          </>
        )}
      </div>
    </>
  )
}

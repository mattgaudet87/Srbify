import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { lookupWord, wordInfo } from '../lib/words.js'
import { useSettings } from '../lib/settings.jsx'
import Sentence from './Sentence.jsx'
import { entryById } from '../lib/search.js'
import CopyButton from './CopyButton.jsx'
import Icon from './Icons.jsx'

const WordContext = createContext({ open: () => {} })
export const useWordCard = () => useContext(WordContext)

const TAG_LABELS = {
  noun: 'Noun', verb: 'Verb', adj: 'Adjective', adv: 'Adverb', pron: 'Pronoun', prep: 'Preposition', conj: 'Connector', particle: 'Little word', interj: 'Phrase / reaction', num: 'Number', name: 'Name',
  casual: 'Casual', formal: 'Formal / polite', flirty: 'Flirty', slang: 'Slang', vulgar: 'Vulgar', culture: 'Culture',
  past: 'Past', present: 'Present', future: 'Future', command: 'Command',
  masc: 'Masculine', fem: 'Feminine', neut: 'Neuter', plural: 'Plural',
}
const KIND = (t) => (['casual', 'formal', 'flirty', 'slang', 'vulgar'].includes(t) ? 'tone' : ['past', 'present', 'future', 'command'].includes(t) ? 'tense' : ['masc', 'fem', 'neut', 'plural'].includes(t) ? 'gender' : 'pos')

// One popup for the whole app. Any <Sentence> word calls open(key).
export function WordProvider({ children }) {
  const [key, setKey] = useState(null)
  const open = useCallback((k) => setKey(k), [])
  const close = useCallback(() => setKey(null), [])
  const value = useMemo(() => ({ open }), [open])
  return (
    <WordContext.Provider value={value}>
      {children}
      {key && <WordSheet wordKey={key} onClose={close} onOpen={open} />}
    </WordContext.Provider>
  )
}

function WordSheet({ wordKey, onClose, onOpen }) {
  const w = lookupWord(wordKey)
  const { settings } = useSettings()
  const sheet = useRef(null)
  const info = useMemo(() => wordInfo(wordKey), [wordKey])

  // Modal behaviour: focus moves into the card, Tab stays inside it, the page behind doesn't scroll, and focus
  // goes back to the tapped word on close.
  useEffect(() => {
    const before = document.activeElement
    const overflow = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    sheet.current?.querySelector('.word-close')?.focus()
    const onKey = (e) => {
      if (e.key === 'Escape') return onClose()
      if (e.key !== 'Tab') return
      const items = [...sheet.current.querySelectorAll('button, a[href]')]
      if (!items.length) return
      const first = items[0], last = items[items.length - 1]
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus() }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus() }
    }
    document.addEventListener('keydown', onKey)
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.style.overflow = overflow
      before?.focus?.()
    }
  }, [onClose])

  useEffect(() => { if (sheet.current) sheet.current.scrollTop = 0 }, [wordKey])

  if (!w) return null
  const entry = w.entry ? entryById[w.entry] : null
  const entryShown = entry && (settings.showVulgar || entry.register !== 'vulgar')
  const used = info.used.map((id) => entryById[id]).filter((e) => e && (settings.showVulgar || e.register !== 'vulgar')).slice(0, 5)
  const base = w.base && lookupWord(w.base) ? w.base : null
  return (
    <div className="sheet-backdrop" onClick={onClose}>
      <div className="word-sheet" ref={sheet} role="dialog" aria-modal="true" aria-label={`Word: ${wordKey}`} onClick={(e) => e.stopPropagation()}>
        <button className="word-close" aria-label="Close" onClick={onClose}><Icon name="x" size={18} strokeWidth={2.4} /></button>
        <p className="word-sr">{wordKey}</p>
        <p className="word-pron">{w.pron}</p>
        <p className="word-en">{w.en}</p>
        {w.note && <p className="word-note">{w.note}</p>}
        <div className="word-tags">
          {w.tags.map((t) => <span key={t} className={`tag tag-${KIND(t)} t-${t}`}>{TAG_LABELS[t] || t}</span>)}
        </div>

        {(base || info.forms.length > 0) && (
          <div className="word-section">
            <h3>{base ? 'Base word' : 'Other forms'}</h3>
            <div className="chips">
              {(base ? [base] : info.forms.slice(0, 8)).map((k) => <button key={k} type="button" className="chip" onClick={() => onOpen(k)}>{k}</button>)}
            </div>
          </div>
        )}

        {info.example && (
          <div className="word-section">
            <h3>In a sentence</h3>
            <p className="word-ex"><Sentence text={info.example.serbian} /></p>
            <p className="word-ex-pron">{info.example.pronunciation}</p>
            <p className="word-ex-en">{info.example.english}</p>
          </div>
        )}

        {used.length > 0 && (
          <div className="word-section">
            <h3>Used in</h3>
            <div className="word-used">
              {used.map((e) => <Link key={e.id} to={`/entry/${e.id}`} onClick={onClose}>{e.serbian}<small>{e.english}</small></Link>)}
            </div>
          </div>
        )}

        <div className="word-actions">
          <CopyButton text={wordKey} small label="Copy" />
          {entryShown && <Link to={`/entry/${entry.id}`} className="word-entry" onClick={onClose}>Open full entry: {entry.english}<Icon name="chevronR" size={16} /></Link>}
        </div>
      </div>
    </div>
  )
}

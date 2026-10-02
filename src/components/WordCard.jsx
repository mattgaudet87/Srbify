import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { lookupWord } from '../lib/words.js'
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
      {key && <WordSheet wordKey={key} onClose={close} />}
    </WordContext.Provider>
  )
}

function WordSheet({ wordKey, onClose }) {
  const w = lookupWord(wordKey)
  useEffect(() => {
    const onKey = (e) => e.key === 'Escape' && onClose()
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [onClose])
  if (!w) return null
  const entry = w.entry ? entryById[w.entry] : null
  return (
    <div className="sheet-backdrop" onClick={onClose}>
      <div className="word-sheet" role="dialog" aria-modal="true" aria-label={`Word: ${wordKey}`} onClick={(e) => e.stopPropagation()}>
        <button className="word-close" aria-label="Close" onClick={onClose}><Icon name="x" size={18} strokeWidth={2.4} /></button>
        <p className="word-sr">{wordKey}</p>
        <p className="word-pron">{w.pron}</p>
        <p className="word-en">{w.en}</p>
        {w.note && <p className="word-note">{w.note}</p>}
        <div className="word-tags">
          {w.tags.map((t) => <span key={t} className={`tag tag-${KIND(t)} t-${t}`}>{TAG_LABELS[t] || t}</span>)}
        </div>
        <div className="word-actions">
          <CopyButton text={wordKey} small label="Copy" />
          {entry && <Link to={`/entry/${entry.id}`} className="word-entry" onClick={onClose}>Open full entry: {entry.english}<Icon name="chevronR" size={16} /></Link>}
        </div>
      </div>
    </div>
  )
}

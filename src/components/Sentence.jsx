import { useMemo } from 'react'
import { tokenize, useWordsReady } from '../lib/words.js'
import { useWordCard } from './WordCard.jsx'

// A Serbian line where every known word (or fixed chunk) opens its word card when tapped.
export default function Sentence({ text, className = '' }) {
  const { open } = useWordCard()
  const ready = useWordsReady()
  const parts = useMemo(() => tokenize(text), [text, ready])
  return (
    <span className={`sentence ${className}`}>
      {parts.map((p, i) => p.key
        ? <button key={i} type="button" className="w" onClick={() => open(p.key)}>{p.text}</button>
        : <span key={i}>{p.text}</span>)}
    </span>
  )
}

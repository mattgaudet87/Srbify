import { useEffect, useState } from 'react'
import Icon from './Icons.jsx'

const synth = typeof window !== 'undefined' ? window.speechSynthesis : null

// Prefer a Serbian voice, then the closest neighbours (Croatian, Bosnian) which read Latin Serbian well.
function pickVoice() {
  const voices = synth?.getVoices() || []
  for (const prefix of ['sr', 'hr', 'bs']) {
    const v = voices.find((x) => x.lang.toLowerCase().replace('_', '-').startsWith(prefix))
    if (v) return v
  }
  return null
}

export default function SpeakButton({ text, small = false }) {
  const [playing, setPlaying] = useState(false)

  // Some browsers load their voice list late.
  useEffect(() => {
    if (!synth) return
    synth.getVoices()
    return () => { if (playing) synth.cancel() }
  }, [playing])

  if (!synth) return null

  function onClick() {
    if (playing) { synth.cancel(); setPlaying(false); return }
    synth.cancel()
    const u = new SpeechSynthesisUtterance(text)
    const v = pickVoice()
    u.lang = v?.lang || 'sr-RS'
    if (v) u.voice = v
    u.rate = 0.85
    u.onend = u.onerror = () => setPlaying(false)
    setPlaying(true)
    synth.speak(u)
  }

  return (
    <button className={`copy speak ${small ? 'small' : ''}`} onClick={onClick} aria-label={playing ? 'Stop' : 'Play pronunciation'}>
      <Icon name={playing ? 'stop' : 'play'} size={small ? 14 : 20} fill="currentColor" />
      <span>{playing ? 'Stop' : 'Play'}</span>
    </button>
  )
}

import { useState } from 'react'
import Icon from './Icons.jsx'

// "Šta ima?" -> "Sta ima?" : strips accents and maps đ to dj, keeps case and punctuation.
export function stripAccents(text) {
  return text
    .replace(/đ/g, 'dj')
    .replace(/Đ/g, 'Dj')
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
}

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text)
    return true
  } catch {
    // Fallback for browsers without the async clipboard API
    const ta = document.createElement('textarea')
    ta.value = text
    ta.style.position = 'fixed'
    ta.style.opacity = '0'
    document.body.appendChild(ta)
    ta.select()
    let ok = false
    try {
      ok = document.execCommand('copy')
    } catch {
      ok = false
    }
    document.body.removeChild(ta)
    return ok
  }
}

export default function CopyButton({ text, plain = false, label, small = false }) {
  const [state, setState] = useState('idle')
  const out = plain ? stripAccents(text) : text

  async function onClick() {
    const ok = await copyText(out)
    setState(ok ? 'done' : 'fail')
    setTimeout(() => setState('idle'), 1500)
  }

  const idle = label || (plain ? 'Copy without accents' : 'Copy')
  return (
    <button className={`copy ${plain ? 'nolatin' : ''} ${small ? 'small' : ''} ${state}`} onClick={onClick} aria-live="polite">
      {!small && <Icon name={state === 'done' ? 'check' : 'copy'} size={20} />}
      <span>{state === 'done' ? 'Copied' : state === 'fail' ? 'Copy failed' : idle}</span>
    </button>
  )
}

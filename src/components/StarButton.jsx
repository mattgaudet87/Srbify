import { useLibrary } from '../lib/library.jsx'
import Icon from './Icons.jsx'

export default function StarButton({ id, className = '' }) {
  const { favorites, toggleFavorite } = useLibrary()
  const on = favorites.includes(id)
  return (
    <button
      type="button"
      className={`star-btn ${on ? 'on' : ''} ${className}`}
      aria-pressed={on}
      aria-label={on ? 'Remove from favorites' : 'Add to favorites'}
      onClick={(ev) => { ev.preventDefault(); ev.stopPropagation(); toggleFavorite(id) }}
    >
      <Icon name="star" size={24} fill={on ? 'currentColor' : 'none'} />
    </button>
  )
}

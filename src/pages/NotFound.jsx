import { Link } from 'react-router-dom'

export default function NotFound() {
  return (
    <>
      <h1 className="title">Page not found</h1>
      <p className="empty">That link doesn’t go anywhere. <Link to="/">Back home</Link> or <Link to="/search">search for a phrase</Link>.</p>
    </>
  )
}

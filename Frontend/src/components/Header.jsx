import { Link, useLocation } from 'react-router-dom'

function Header({ theme, toggleTheme }) {
  const location = useLocation()

  const isActive = (path) =>
    location.pathname === path ? 'active' : ''

  return (
    <header className="header">
      <div className="header-inner">
        <Link to="/" className="site-name">
          Madhav Khanal
        </Link>
        <nav className="nav">
          <Link to="/blog" className={isActive('/blog')}>Blog</Link>
          <Link to="/papers" className={isActive('/papers')}>Papers</Link>
          <Link to="/about" className={isActive('/about')}>About</Link>
          <Link to="/life" className={isActive('/life')}>Life</Link>
          <button onClick={toggleTheme} className="theme-btn">
            {theme === 'light' ? 'dark' : 'light'}
          </button>
        </nav>
      </div>
    </header>
  )
}

export default Header
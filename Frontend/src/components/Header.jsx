import { Link, useLocation } from 'react-router-dom'

function Header({ theme, toggleTheme }) {
  const location = useLocation()

  const isActive = (path) => {
    return location.pathname === path ? 'active' : ''
  }

  return (
    <header className="header">
      <div className="header-content">
        <Link to="/" className="logo">
          Madhav Khanal
        </Link>
        <nav className="nav">
          <Link to="/blog" className={isActive('/blog')}>
            Blog
          </Link>
          <Link to="/about" className={isActive('/about')}>
            About
          </Link>
          <button onClick={toggleTheme} className="theme-toggle">
            {theme === 'light' ? 'Dark' : 'Light'}
          </button>
        </nav>
      </div>
    </header>
  )
}

export default Header
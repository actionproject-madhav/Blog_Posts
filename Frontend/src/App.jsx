import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom'
import { useState, useEffect } from 'react'
import Spline from '@splinetool/react-spline'
import Header from './components/Header'
import Home from './pages/Home'
import BlogList from './pages/BlogList'
import BlogPost from './components/BlogPost'
import About from './pages/About'
import Admin from './pages/Admin'

function AppContent({ theme, setTheme, toggleTheme }) {
  const location = useLocation()
  const showSpline = location.pathname === '/' || location.pathname === '/about'

  // Different Spline scenes for different pages
  const getSplineScene = () => {
    if (location.pathname === '/') {
      return "https://prod.spline.design/J6tsAlAO6E4HY7Wq/scene.splinecode"
    } else if (location.pathname === '/about') {
      return "https://prod.spline.design/Anob6XCn921GlqBo/scene.splinecode"
    }
    return null
  }

  return (
    <div className="app">
      {/* Fixed Spline background for entire page */}
      {showSpline && (
        <div className="spline-full-background">
          <Spline
            scene={getSplineScene()}
          />
          <div className="spline-watermark-overlay"></div>
        </div>
      )}
      <Header theme={theme} toggleTheme={toggleTheme} />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/blog" element={<BlogList />} />
          <Route path="/blog/:slug" element={<BlogPost />} />
          <Route path="/about" element={<About />} />
          <Route path="/admin" element={<Admin />} />

        </Routes>
      </main>
      <footer className="footer">
        <p>© {new Date().getFullYear()} Madhav Khanal. All rights reserved.</p>
      </footer>
    </div>
  )
}

function App() {
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme')
    return saved || 'light'
  })

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('theme', theme)
  }, [theme])

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light')
  }

  return (
    <Router>
      <AppContent theme={theme} setTheme={setTheme} toggleTheme={toggleTheme} />
    </Router>
  )
}

export default App
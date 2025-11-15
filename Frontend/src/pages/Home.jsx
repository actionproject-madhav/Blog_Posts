import { Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
import Spline from '@splinetool/react-spline'
import BlogCard from '../components/BlogCard'
import { getAllPosts } from '../utils/markdown'

function Home() {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    getAllPosts().then(allPosts => {
      setPosts(allPosts.slice(0, 3))
    })
  }, [])

  return (
    <div>
      <section className="hero hero-with-spline">
        <div className="hero-content">
          <h1>Math, CS, and Puzzles</h1>
          <p>
            Exploring algorithms, mathematics, and problem-solving through clear explanations and interactive visualizations.
          </p>
        </div>
        
        <div className="spline-container">
          <Spline
            scene="https://prod.spline.design/J6tsAlAO6E4HY7Wq/scene.splinecode"
          />
          {/* Watermark workaround - darken/blur bottom right corner */}
          <div className="spline-watermark-overlay"></div>
        </div>
      </section>

      <section style={{ marginTop: '80px' }}>
        <h2 style={{ fontSize: '28px', marginBottom: '20px', fontWeight: '600' }}>
          Recent Posts
        </h2>
        <div className="blog-grid">
          {posts.map(post => (
            <BlogCard key={post.slug} post={post} />
          ))}
        </div>
        {posts.length > 0 && (
          <div style={{ marginTop: '40px' }}>
            <Link 
              to="/blog" 
              style={{ 
                color: 'var(--text-primary)', 
                textDecoration: 'underline',
                fontSize: '16px'
              }}
            >
              View all posts →
            </Link>
          </div>
        )}
      </section>
    </div>
  )
}

export default Home
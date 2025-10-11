import { Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
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
      <section className="hero">
        <h1>Math, CS, and Puzzles</h1>
        <p>
          Math and Computer Science Undergrad student exploring algorithms, mathematics, and problem-solving. 
          Writing short posts with clear explanations and animations.
        </p>
      </section>

      <section>
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
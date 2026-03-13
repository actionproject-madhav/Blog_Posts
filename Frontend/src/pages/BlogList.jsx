import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { getAllPosts } from '../utils/markdown'

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric', month: 'short', day: 'numeric'
  })
}

function BlogList() {
  const [posts, setPosts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getAllPosts().then(allPosts => {
      setPosts(allPosts)
      setLoading(false)
    })
  }, [])

  if (loading) {
    return (
      <div className="blog-list-page">
        <p style={{ color: 'var(--text-3)', fontSize: '14px' }}>Loading…</p>
      </div>
    )
  }

  return (
    <div className="blog-list-page">
      <h1 className="page-heading">Writing</h1>
      {posts.length === 0 ? (
        <p style={{ color: 'var(--text-3)', fontSize: '14px' }}>No posts yet. Check back soon!</p>
      ) : (
        <ul className="post-list">
          {posts.map(post => (
            <li key={post.slug} className="post-list-item">
              <span className="post-list-date">{formatDate(post.date)}</span>
              <Link to={`/blog/${post.slug}`} className="post-list-title">
                {post.title}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default BlogList
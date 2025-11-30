import { useState, useEffect } from 'react'
import BlogCard from '../components/BlogCard'
import { getAllPosts } from '../utils/markdown'

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
    return <div>Loading posts...</div>
  }

  return (
    <div style={{ background: 'var(--bg-primary)', padding: '40px 0', minHeight: '100vh' }}>
      <h1 style={{ fontSize: '24px', marginBottom: '20px', fontWeight: '500' }}>
        All Posts
      </h1>
      <div className="blog-grid">
        {posts.length === 0 ? (
          <p style={{ color: 'var(--text-secondary)' }}>
            No posts yet. Check back soon!
          </p>
        ) : (
          posts.map(post => (
            <BlogCard key={post.slug} post={post} />
          ))
        )}
      </div>
    </div>
  )
}

export default BlogList
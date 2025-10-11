import { Link } from 'react-router-dom'

function BlogCard({ post }) {
  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' }
    return new Date(dateString).toLocaleDateString('en-US', options)
  }

  return (
    <Link to={`/blog/${post.slug}`} className="blog-card">
      <h2>{post.title}</h2>
      <div className="blog-card-meta">
        {formatDate(post.date)}
      </div>
      <p className="blog-card-excerpt">{post.excerpt}</p>
      {post.tags && post.tags.length > 0 && (
        <div className="blog-card-tags">
          {post.tags.map((tag, index) => (
            <span key={index} className="tag">
              {tag}
            </span>
          ))}
        </div>
      )}
    </Link>
  )
}

export default BlogCard
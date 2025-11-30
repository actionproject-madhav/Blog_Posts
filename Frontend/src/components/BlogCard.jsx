import { Link } from 'react-router-dom'

function BlogCard({ post }) {
  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' }
    return new Date(dateString).toLocaleDateString('en-US', options)
  }

  return (
    <Link to={`/blog/${post.slug}`} className="blog-card">
      <h2>{post.title}</h2>
      <span className="blog-card-meta">
        {formatDate(post.date)}
      </span>
    </Link>
  )
}

export default BlogCard
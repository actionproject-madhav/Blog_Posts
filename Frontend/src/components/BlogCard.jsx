import { Link } from 'react-router-dom'

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric', month: 'short', day: 'numeric'
  })
}

function BlogCard({ post }) {
  return (
    <li className="post-list-item">
      <span className="post-list-date">{formatDate(post.date)}</span>
      <Link to={`/blog/${post.slug}`} className="post-list-title">
        {post.title}
      </Link>
    </li>
  )
}

export default BlogCard
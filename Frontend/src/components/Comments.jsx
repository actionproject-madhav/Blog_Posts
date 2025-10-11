import { useState, useEffect } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

function Comments({ postSlug }) {
  const [comments, setComments] = useState([])
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [formData, setFormData] = useState({
    author_name: '',
    content: ''
  })
  const [message, setMessage] = useState(null)

  useEffect(() => {
    fetchComments()
  }, [postSlug])

  const fetchComments = async () => {
    try {
      const response = await fetch(`${API_URL}/api/comments/${postSlug}`)
      const data = await response.json()
      if (data.success) {
        setComments(data.comments)
      }
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setSubmitting(true)
    setMessage(null)

    try {
      const response = await fetch(`${API_URL}/api/comments`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          post_slug: postSlug,
          ...formData
        })
      })

      const data = await response.json()

      if (data.success) {
        setMessage({ type: 'success', text: 'Comment posted!' })
        setFormData({ author_name: '', content: '' })
        fetchComments()
      } else {
        setMessage({ type: 'error', text: data.error })
      }
    } catch (error) {
      setMessage({ type: 'error', text: 'Failed to post comment' })
    } finally {
      setSubmitting(false)
    }
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    })
  }

  return (
    <div className="comments-section">
      <h3>Comments ({comments.length})</h3>

      {/* Comment Form */}
      <form onSubmit={handleSubmit} className="comment-form">
        <input
          type="text"
          placeholder="Your name"
          value={formData.author_name}
          onChange={(e) => setFormData({ ...formData, author_name: e.target.value })}
          required
          className="comment-input"
        />
        <textarea
          placeholder="Write your comment..."
          value={formData.content}
          onChange={(e) => setFormData({ ...formData, content: e.target.value })}
          required
          rows="4"
          className="comment-textarea"
        />
        {message && (
          <div className={`comment-message ${message.type}`}>
            {message.text}
          </div>
        )}
        <button type="submit" disabled={submitting} className="comment-submit">
          {submitting ? 'Posting...' : 'Post Comment'}
        </button>
      </form>

      {/* Comments List */}
      <div className="comments-list">
        {loading ? (
          <p>Loading...</p>
        ) : comments.length === 0 ? (
          <p>No comments yet. Be the first!</p>
        ) : (
          comments.map((comment) => (
            <div key={comment._id} className="comment">
              <div className="comment-header">
                <strong>{comment.author_name}</strong>
                <span className="comment-date">{formatDate(comment.created_at)}</span>
              </div>
              <p className="comment-content">{comment.content}</p>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default Comments
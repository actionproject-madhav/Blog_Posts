import { useState } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

function CommentForm({ postSlug, parentId = null, onCommentAdded, onCancel }) {
  const [formData, setFormData] = useState({
    author_name: '',
    author_email: '',
    content: ''
  })
  const [submitting, setSubmitting] = useState(false)
  const [message, setMessage] = useState(null)

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
    setMessage(null)
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
          parent_id: parentId,
          ...formData
        })
      })

      const data = await response.json()

      if (data.success) {
        setMessage({
          type: 'success',
          text: 'Comment posted successfully!'
        })
        setFormData({ author_name: '', author_email: '', content: '' })
        if (onCommentAdded) onCommentAdded()
      } else {
        setMessage({
          type: 'error',
          text: data.error || 'Failed to post comment'
        })
      }
    } catch (error) {
      setMessage({
        type: 'error',
        text: 'Network error. Please try again.'
      })
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className={`comment-form ${parentId ? 'comment-form-reply' : ''}`}>
      <div className="comment-form-grid">
        <input
          type="text"
          name="author_name"
          placeholder="Your name *"
          value={formData.author_name}
          onChange={handleChange}
          required
          minLength="2"
          maxLength="50"
          className="comment-input"
        />
        <input
          type="email"
          name="author_email"
          placeholder="Email (optional, won't be published)"
          value={formData.author_email}
          onChange={handleChange}
          className="comment-input"
        />
      </div>
      <textarea
        name="content"
        placeholder={parentId ? "Write your reply..." : "Share your thoughts..."}
        value={formData.content}
        onChange={handleChange}
        required
        rows="4"
        minLength="3"
        maxLength="2000"
        className="comment-textarea"
      />
      {message && (
        <div className={`comment-message ${message.type}`}>
          {message.text}
        </div>
      )}
      <div className="comment-form-actions">
        <button 
          type="submit" 
          disabled={submitting}
          className="comment-submit"
        >
          {submitting ? 'Posting...' : (parentId ? 'Post Reply' : 'Post Comment')}
        </button>
        {onCancel && (
          <button 
            type="button"
            onClick={onCancel}
            className="comment-cancel"
          >
            Cancel
          </button>
        )}
      </div>
    </form>
  )
}

export default CommentForm
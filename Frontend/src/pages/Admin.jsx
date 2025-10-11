import { useState, useEffect } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

function Admin() {
  const [comments, setComments] = useState([])
  const [loading, setLoading] = useState(true)
  const [credentials, setCredentials] = useState({ username: '', password: '' })
  const [authenticated, setAuthenticated] = useState(false)
  const [stats, setStats] = useState({ total: 0, pending: 0, approved: 0 })

  const fetchComments = async () => {
    try {
      const response = await fetch(`${API_URL}/api/admin/comments`, {
        headers: {
          'Authorization': 'Basic ' + btoa(`${credentials.username}:${credentials.password}`)
        }
      })
      
      if (response.status === 401) {
        setAuthenticated(false)
        return
      }

      const data = await response.json()
      if (data.success) {
        setComments(data.comments)
        calculateStats(data.comments)
        setAuthenticated(true)
      }
    } catch (error) {
      console.error('Error fetching comments:', error)
    } finally {
      setLoading(false)
    }
  }

  const calculateStats = (comments) => {
    setStats({
      total: comments.length,
      pending: comments.filter(c => !c.is_approved).length,
      approved: comments.filter(c => c.is_approved).length
    })
  }

  const handleLogin = (e) => {
    e.preventDefault()
    setLoading(true)
    fetchComments()
  }

  const handleApprove = async (commentId) => {
    try {
      const response = await fetch(`${API_URL}/api/admin/comments/${commentId}/approve`, {
        method: 'POST',
        headers: {
          'Authorization': 'Basic ' + btoa(`${credentials.username}:${credentials.password}`)
        }
      })

      if (response.ok) {
        fetchComments()
      }
    } catch (error) {
      console.error('Error approving comment:', error)
    }
  }

  const handleDelete = async (commentId) => {
    if (!confirm('Are you sure you want to delete this comment?')) return

    try {
      const response = await fetch(`${API_URL}/api/admin/comments/${commentId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': 'Basic ' + btoa(`${credentials.username}:${credentials.password}`)
        }
      })

      if (response.ok) {
        fetchComments()
      }
    } catch (error) {
      console.error('Error deleting comment:', error)
    }
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  if (!authenticated) {
    return (
      <div className="admin-container">
        <div className="admin-login">
          <h1>Admin Login</h1>
          <form onSubmit={handleLogin}>
            <input
              type="text"
              placeholder="Username"
              value={credentials.username}
              onChange={(e) => setCredentials({ ...credentials, username: e.target.value })}
              required
              className="admin-input"
            />
            <input
              type="password"
              placeholder="Password"
              value={credentials.password}
              onChange={(e) => setCredentials({ ...credentials, password: e.target.value })}
              required
              className="admin-input"
            />
            <button type="submit" className="admin-btn-primary">
              {loading ? 'Logging in...' : 'Login'}
            </button>
          </form>
        </div>
      </div>
    )
  }

  return (
    <div className="admin-container">
      <div className="admin-header">
        <h1>Comment Moderation</h1>
        <button 
          onClick={() => setAuthenticated(false)}
          className="admin-btn-secondary"
        >
          Logout
        </button>
      </div>

      <div className="admin-stats">
        <div className="admin-stat-card">
          <div className="admin-stat-number">{stats.total}</div>
          <div className="admin-stat-label">Total Comments</div>
        </div>
        <div className="admin-stat-card">
          <div className="admin-stat-number">{stats.approved}</div>
          <div className="admin-stat-label">Approved</div>
        </div>
        <div className="admin-stat-card">
          <div className="admin-stat-number">{stats.pending}</div>
          <div className="admin-stat-label">Pending</div>
        </div>
      </div>

      <div className="admin-comments">
        {loading ? (
          <p>Loading comments...</p>
        ) : comments.length === 0 ? (
          <p className="admin-empty">No comments yet.</p>
        ) : (
          comments.map((comment) => (
            <div 
              key={comment._id} 
              className={`admin-comment ${!comment.is_approved ? 'admin-comment-pending' : ''}`}
            >
              <div className="admin-comment-header">
                <div>
                  <strong>{comment.author_name}</strong>
                  {comment.author_type === 'google' && <span className="admin-verified">✓</span>}
                  <span className="admin-comment-email">
                    {comment.author_email && `(${comment.author_email})`}
                  </span>
                </div>
                <div className="admin-comment-meta">
                  <span className="admin-comment-post">Post: {comment.post_slug}</span>
                  <span className="admin-comment-date">{formatDate(comment.created_at)}</span>
                </div>
              </div>
              
              <p className="admin-comment-content">{comment.content}</p>

              <div className="admin-comment-footer">
                <div className="admin-comment-stats">
                  <span>♥ {comment.likes} likes</span>
                  {comment.parent_id && <span>↳ Reply</span>}
                </div>
                <div className="admin-comment-actions">
                  {!comment.is_approved && (
                    <button
                      onClick={() => handleApprove(comment._id)}
                      className="admin-btn-approve"
                    >
                      Approve
                    </button>
                  )}
                  <button
                    onClick={() => handleDelete(comment._id)}
                    className="admin-btn-delete"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default Admin
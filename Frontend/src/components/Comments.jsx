import { useState, useEffect } from 'react'
import CommentForm from './CommentForm'
import CommentItem from './CommentItem'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

function Comments({ postSlug }) {
  const [comments, setComments] = useState([])
  const [loading, setLoading] = useState(true)
  const [replyingTo, setReplyingTo] = useState(null)

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
      console.error('Error fetching comments:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleCommentAdded = () => {
    fetchComments()
    setReplyingTo(null)
  }

  const handleLike = async (commentId) => {
    try {
      const response = await fetch(`${API_URL}/api/comments/${commentId}/like`, {
        method: 'POST'
      })
      const data = await response.json()
      if (data.success) {
        // Update comment likes in state
        fetchComments()
      }
    } catch (error) {
      console.error('Error liking comment:', error)
    }
  }

  return (
    <div className="comments-section">
      <h3 className="comments-title">
        Comments {comments.length > 0 && `(${comments.length})`}
      </h3>

      <CommentForm 
        postSlug={postSlug}
        onCommentAdded={handleCommentAdded}
      />

      <div className="comments-list">
        {loading ? (
          <p className="comments-loading">Loading comments...</p>
        ) : comments.length === 0 ? (
          <p className="comments-empty">
            No comments yet. Be the first to share your thoughts!
          </p>
        ) : (
          comments.map((comment) => (
            <CommentItem
              key={comment._id}
              comment={comment}
              onReply={setReplyingTo}
              onLike={handleLike}
              replyingTo={replyingTo}
              postSlug={postSlug}
              onCommentAdded={handleCommentAdded}
            />
          ))
        )}
      </div>
    </div>
  )
}

export default Comments
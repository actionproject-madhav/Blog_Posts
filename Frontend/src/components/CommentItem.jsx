import { useState } from 'react'
import CommentForm from './CommentForm'

function CommentItem({ comment, onReply, onLike, replyingTo, postSlug, onCommentAdded }) {
  const [showReplies, setShowReplies] = useState(true)

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    const now = new Date()
    const diffMs = now - date
    const diffMins = Math.floor(diffMs / 60000)
    const diffHours = Math.floor(diffMs / 3600000)
    const diffDays = Math.floor(diffMs / 86400000)

    if (diffMins < 1) return 'just now'
    if (diffMins < 60) return `${diffMins}m ago`
    if (diffHours < 24) return `${diffHours}h ago`
    if (diffDays < 7) return `${diffDays}d ago`
    
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined
    })
  }

  const isReplyFormOpen = replyingTo === comment._id

  return (
    <div className="comment">
      <div className="comment-header">
        <div className="comment-author-info">
          <strong className="comment-author">
            {comment.author_name}
          </strong>
          {comment.author_type === 'google' && (
            <span className="comment-verified" title="Verified with Google">✓</span>
          )}
          <span className="comment-date">{formatDate(comment.created_at)}</span>
        </div>
        <div className="comment-actions">
          <button 
            onClick={() => onLike(comment._id)}
            className="comment-like-btn"
            title="Like this comment"
          >
            ♥ {comment.likes > 0 && comment.likes}
          </button>
        </div>
      </div>
      
      <p className="comment-content">{comment.content}</p>

      <div className="comment-footer">
        <button
          onClick={() => onReply(isReplyFormOpen ? null : comment._id)}
          className="comment-reply-btn"
        >
          {isReplyFormOpen ? 'Cancel' : 'Reply'}
        </button>
        {comment.replies && comment.replies.length > 0 && (
          <button
            onClick={() => setShowReplies(!showReplies)}
            className="comment-toggle-replies"
          >
            {showReplies ? 'Hide' : 'Show'} {comment.replies.length} {comment.replies.length === 1 ? 'reply' : 'replies'}
          </button>
        )}
      </div>

      {isReplyFormOpen && (
        <CommentForm
          postSlug={postSlug}
          parentId={comment._id}
          onCommentAdded={onCommentAdded}
          onCancel={() => onReply(null)}
        />
      )}

      {comment.replies && comment.replies.length > 0 && showReplies && (
        <div className="comment-replies">
          {comment.replies.map((reply) => (
            <CommentItem
              key={reply._id}
              comment={reply}
              onReply={onReply}
              onLike={onLike}
              replyingTo={replyingTo}
              postSlug={postSlug}
              onCommentAdded={onCommentAdded}
            />
          ))}
        </div>
      )}
    </div>
  )
}

export default CommentItem
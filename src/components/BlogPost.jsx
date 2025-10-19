import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'
import rehypeKatex from 'rehype-katex'
import rehypeRaw from 'rehype-raw'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark, oneLight } from 'react-syntax-highlighter/dist/esm/styles/prism'
import matter from 'gray-matter'
import comments from './comments'

function BlogPost() {
  const { slug } = useParams()
  const [post, setPost] = useState(null)
  const [loading, setLoading] = useState(true)
  const theme = document.documentElement.getAttribute('data-theme')

  useEffect(() => {
    fetch(`/posts/${slug}.md`)
      .then(res => res.text())
      .then(text => {
        const { data, content } = matter(text)
        setPost({ ...data, content })
        setLoading(false)
      })
      .catch(() => {
        setPost(null)
        setLoading(false)
      })
  }, [slug])

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' }
    return new Date(dateString).toLocaleDateString('en-US', options)
  }

  if (loading) {
    return <div>Loading...</div>
  }

  if (!post) {
    return <div>Post not found</div>
  }

  return (
    <article className="blog-content">
      <div className="blog-header">
        <h1>{post.title}</h1>
        <div className="blog-meta">
          {formatDate(post.date)}
        </div>
        {post.tags && post.tags.length > 0 && (
          <div className="blog-card-tags" style={{ marginTop: '16px' }}>
            {post.tags.map((tag, index) => (
              <span key={index} className="tag">
                {tag}
              </span>
            ))}
          </div>
        )}
      </div>
      <div className="markdown-content">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeKatex, rehypeRaw]}
          components={{
            code({ node, inline, className, children, ...props }) {
              const match = /language-(\w+)/.exec(className || '')
              return !inline && match ? (
                <SyntaxHighlighter
                  style={theme === 'dark' ? oneDark : oneLight}
                  language={match[1]}
                  PreTag="div"
                  {...props}
                >
                  {String(children).replace(/\n$/, '')}
                </SyntaxHighlighter>
              ) : (
                <code className={className} {...props}>
                  {children}
                </code>
              )
            }
          }}
        >
          {post.content}
        </ReactMarkdown>
      </div>
      <comments />
    </article>
  )
}

export default BlogPost
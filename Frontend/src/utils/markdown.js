import matter from 'gray-matter'

export async function getAllPosts() {
  try {
    const response = await fetch('/posts/posts.json')
    const manifest = await response.json()
    
    const posts = await Promise.all(
      manifest.posts.map(async (slug) => {
        try {
          const response = await fetch(`/posts/${slug}.md`)
          const text = await response.text()
          const { data } = matter(text)
          
          // Validate required fields
          if (!data.title || !data.date) {
            console.warn(`Post ${slug} is missing required fields (title or date)`)
            return null
          }
          
          return {
            slug,
            title: data.title,
            date: data.date,
            excerpt: data.excerpt || '',
            tags: data.tags || [],
          }
        } catch (error) {
          console.error(`Error loading post ${slug}:`, error)
          return null
        }
      })
    )

    const validPosts = posts.filter(post => post !== null && post.title && post.date)
    console.log(`Loaded ${validPosts.length} posts:`, validPosts.map(p => p.slug))
    
    return validPosts.sort((a, b) => {
      const dateA = new Date(a.date)
      const dateB = new Date(b.date)
      if (isNaN(dateA.getTime()) || isNaN(dateB.getTime())) {
        return 0
      }
      return dateB - dateA
    })
  } catch (error) {
    console.error('Error loading posts manifest:', error)
    return []
  }
}
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
          
          return {
            slug,
            title: data.title,
            date: data.date,
            excerpt: data.excerpt,
            tags: data.tags || [],
          }
        } catch (error) {
          console.error(`Error loading post ${slug}:`, error)
          return null
        }
      })
    )

    return posts
      .filter(post => post !== null)
      .sort((a, b) => new Date(b.date) - new Date(a.date))
  } catch (error) {
    console.error('Error loading posts manifest:', error)
    return []
  }
}
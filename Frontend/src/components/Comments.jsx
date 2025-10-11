function Comments() {
  return (
    <div style={{ marginTop: '60px', paddingTop: '40px', borderTop: '1px solid var(--border)' }}>
      <h3 style={{ fontSize: '24px', marginBottom: '20px', fontWeight: '600' }}>Comments</h3>
      <script
        src="https://giscus.app/client.js"
        data-repo="yourusername/madhav-blog"
        data-repo-id="YOUR_REPO_ID"
        data-category="General"
        data-category-id="YOUR_CATEGORY_ID"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async
      />
    </div>
  )
}

export default Comments
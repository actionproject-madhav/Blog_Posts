
const lifeItems = [
  {
    title: 'Nature and Meditation',
    desc: 'Certified meditation trainer, learnt meditation from Gurus for a year across the Himlayas after my high school',
    image: '/meditation.jpeg'
  },
  {
    title: 'Robotics',
    desc: 'Building and programming autonomous systems that interact with the physical world.',
    image: '/zpm.png'
  },

  {
    title: 'Creativity',
    desc: 'Deep Passion for literature, writing and poetry. Check out my novel: ',
    link: 'https://heritagebooks.com.np/product/abichal-karmayoddha/',
    image: '/literature.jpg'
  }
]

function Life() {
  return (
    <div className="life-page">
      <h1 className="page-heading">Life</h1>
      <p className="papers-intro">
        A collection of hobbies, interests, and moments outside of research and code.
      </p>

      <div className="life-content">
        {lifeItems.map((item, index) => (
          <div key={index} className="life-item">
            <img src={item.image} alt={item.title} className="life-image" />
            <h2 className="life-title">{item.title}</h2>
            <p className="life-desc">
              {item.desc}
              {item.link && (
                <a 
                  href={item.link} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="life-link"
                >
                  Link →
                </a>
              )}
            </p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Life

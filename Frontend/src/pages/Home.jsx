import { Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
import { getAllPosts } from '../utils/markdown'

function formatDate(dateString) {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
}

const featuredProjects = [
  {
    title: 'Finlit',
    desc: 'Winning NSA AI Hackathon platform for financial literacy.',
    image: '/finlit.jpeg',
    link: 'https://finlit-sigma.vercel.app'
  },
  {
    title: 'Zero Panic in Movement',
    desc: 'Autonomous robot swarm for emergency evacuation.',
    image: '/zpm.png',
    link: 'https://devpost.com/software/zero-panic-in-movement-zpm'
  },
  {
    title: 'CuraSyn+',
    desc: 'Real-time stroke detection using Computer Vision and AI.',
    image: '/curasyn.jpeg',
    link: 'https://curasyn.onrender.com'
  }
]

const selectedPapers = [
  {
    title: 'Bridging the Gap Between Theory and Practice in Adversarial ML',
    year: '2025',
    desc: 'Analyzing the disconnect between theoretical guarantees and practical attacks.',
    tag: 'Robustness'
  },
  {
    title: 'Using Large Language Models for Rubric Based Assessment',
    year: '2025',
    desc: 'Research on LLMs as automated graders and their failure modes.',
    tag: 'Evaluation'
  }
]

function Home() {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    getAllPosts().then(allPosts => {
      setPosts(allPosts.slice(0, 3))
    })
  }, [])

  return (
    <div className="home-page">
      {/* Intro */}
      <section className="intro">
        <div className="intro-name">
          <img
            src="/profile.jpeg"
            alt="Madhav Khanal"
            className="intro-photo"
            onError={e => { e.target.style.display = 'none' }}
          />
          Madhav Khanal
        </div>
        <p className="intro-bio">
          Math and CS double major at Rollins College on a full-ride Alfond Scholarship.
          Former IPhO national team member for Nepal. Interested in empirical evaluation
          and robustness of ML systems. Currently doing AI safety research at{' '}
          <a href="https://saferai.org" target="_blank" rel="noopener noreferrer">Safer AI</a>{' '}
          via SPAR.
        </p>
        <div className="intro-links">
          <a href="https://github.com/actionproject-madhav" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a href="https://linkedin.com/in/madhav-khanal3145/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          <a href="mailto:mkhanal@rollins.edu">Email</a>
          <a href="/papers/Madhav_Cv (13).pdf" download>CV</a>
        </div>
      </section>

      {/* Focus */}
      <section className="home-section">
        <p className="home-section-title">Focus</p>
        <div className="focus-block">
          <span className="focus-tag">Working on</span>
          <p style={{ margin: 0, fontSize: '15px', lineHeight: '1.6', color: 'var(--text-2)' }}>
            Reducing the gap between research and deployment in <strong>Adversarial ML</strong>. 
            Currently evaluating ML robustness and benchmark transferability for deployed systems.
          </p>
        </div>
      </section>

      {/* Papers Snapshot */}
      <section className="home-section">
        <p className="home-section-title">Selected Papers</p>
        <div className="papers-snapshot">
          {selectedPapers.map(paper => (
            <div key={paper.title} className="paper-snapshot-item">
              <div className="paper-snapshot-meta">{paper.year} · {paper.tag}</div>
              <Link to="/papers" className="paper-snapshot-title">{paper.title}</Link>
              <p className="paper-snapshot-desc">{paper.desc}</p>
            </div>
          ))}
        </div>
        <Link to="/papers" className="view-all">All papers →</Link>
      </section>

      {/* Projects */}
      <section className="home-section">
        <p className="home-section-title">Selected Projects</p>
        <div className="project-grid">
          {featuredProjects.map(project => (
            <a key={project.title} href={project.link} target="_blank" rel="noopener noreferrer" className="project-tile">
              <div className="project-img-wrap">
                <img src={project.image} alt={project.title} className="project-img" />
              </div>
              <div className="project-tile-title">{project.title}</div>
              <div className="project-tile-desc">{project.desc}</div>
            </a>
          ))}
        </div>
        <Link to="/about" className="view-all">View all work →</Link>
      </section>

      {/* Recent posts */}
      {posts.length > 0 && (
        <section className="home-section" style={{ paddingBottom: '80px' }}>
          <p className="home-section-title">Writing</p>
          <ul className="post-list">
            {posts.map(post => (
              <li key={post.slug} className="post-list-item">
                <span className="post-list-date">{formatDate(post.date)}</span>
                <Link to={`/blog/${post.slug}`} className="post-list-title">
                  {post.title}
                </Link>
              </li>
            ))}
          </ul>
          <Link to="/blog" className="view-all">View all posts →</Link>
        </section>
      )}
    </div>
  )
}

export default Home
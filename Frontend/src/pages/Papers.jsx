import { useState } from 'react'

const papers = [
  {
    id: 'adversarial-ml',
    title: 'Bridging the Gap Between Theory and Practice in Adversarial Machine Learning',
    year: '2025',
    description:
      'An analysis of the disconnect between theoretical adversarial ML guarantees and real-world practical attacks, with proposed frameworks for closing this gap.',
    tags: ['Adversarial ML', 'Deep Learning', 'Robustness'],
    file: '/papers/Bridging the Gap Between Theory and Practice in Adversarial ML (1).pdf',
  },
  {
    id: 'metacrisp',
    title: 'MetaCRISP 2026 — Paper 12',
    year: '2026',
    description:
      'Under review at MetaCRISP 2026. Explores meta-learning approaches and crisp reasoning systems.',
    tags: ['Meta-learning', 'Under Review'],
    file: '/papers/metacrisp26-paper12 (1) (1).pdf',
  },
  {
    id: 'ai-eval',
    title: 'Using Large Language Models for Rubric Based Assessment',
    year: '2025',
    description:
      'Research poster on using LLMs as automated graders, evaluating their performance and failure modes against human rubric-based assessment.',
    tags: ['LLM Evaluation', 'AI Safety', 'Poster'],
    file: '/papers/AI Eval Poster.pptx.pdf',
  },
]

function Papers() {
  const [activePaper, setActivePaper] = useState(null)

  const openPaper = (paper) => {
    setActivePaper(paper)
    // scroll to viewer
    setTimeout(() => {
      document.getElementById('pdf-viewer')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }, 50)
  }

  const closePaper = () => {
    setActivePaper(null)
    document.getElementById('papers-list')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <div className="papers-page">
      <h1 className="page-heading">Papers</h1>
      <p className="papers-intro">
        Research and writing. Click any paper to read it here.
      </p>

      {/* Paper list */}
      <div id="papers-list" className="papers-list">
        {papers.map((paper) => (
          <div
            key={paper.id}
            className={`paper-entry ${activePaper?.id === paper.id ? 'paper-entry--active' : ''}`}
          >
            <div className="paper-entry-header">
              <div className="paper-entry-meta">{paper.year}</div>
              <button
                className="paper-entry-title"
                onClick={() => activePaper?.id === paper.id ? closePaper() : openPaper(paper)}
              >
                {paper.title}
                <span className="paper-open-icon">
                  {activePaper?.id === paper.id ? '↑ close' : '↓ read'}
                </span>
              </button>
              <p className="paper-entry-desc">{paper.description}</p>
              <div className="entry-tags">
                {paper.tags.map(t => <span key={t} className="tag">{t}</span>)}
              </div>
            </div>

            {/* Inline viewer — only for the active paper */}
            {activePaper?.id === paper.id && (
              <div id="pdf-viewer" className="pdf-viewer-wrap">
                <div className="pdf-viewer-toolbar">
                  <span className="pdf-viewer-title">{paper.title}</span>
                  <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
                    <a
                      href={paper.file}
                      download
                      className="pdf-download-btn"
                    >
                      ↓ Download
                    </a>
                    <button onClick={closePaper} className="pdf-close-btn">✕</button>
                  </div>
                </div>
                <iframe
                  src={paper.file}
                  title={paper.title}
                  className="pdf-iframe"
                />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}

export default Papers

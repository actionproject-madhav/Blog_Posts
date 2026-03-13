function About() {
  return (
    <div className="about-page">

      {/* Header */}
      <div className="about-header">
        <img
          src="/profile.jpeg"
          alt="Madhav Khanal"
          className="about-photo"
          onError={e => { e.target.style.display = 'none' }}
        />
        <div>
          <h1 className="about-name">Madhav Khanal</h1>
          <p className="about-subtitle">CS &amp; Math, Rollins College · Alfond Scholar</p>
          <div className="about-links">
            <a href="https://github.com/actionproject-madhav" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a href="https://linkedin.com/in/madhav-khanal3145/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="mailto:mkhanal@rollins.edu">Email</a>
            <a href="/resume.pdf" download>CV</a>
          </div>
        </div>
      </div>

      {/* Research focus */}
      <div className="about-section">
        <p className="about-section-title">Research</p>
        <p>
          My goal is to pursue a PhD in empirical evaluation and robustness of machine learning
          systems deployed in the real world. My prior work revolves around evaluating LLMs on
          different domains, analyzing the gap between research and industry in adversarial
          machine learning, and quantitative risk modelling of deployed ML systems.
        </p>
        <p>
          Currently doing AI safety research through{' '}
          <a href="https://saferai.org" target="_blank" rel="noopener noreferrer">Safer AI</a>{' '}
          via the SPAR program. Former IPhO national team member for Nepal (53rd IPhO, Japan).
          Full-ride Alfond Scholar at Rollins College, 4.0 GPA.
        </p>
      </div>

      {/* Experience */}
      <div className="about-section">
        <p className="about-section-title">Experience</p>

        <div className="entry">
          <div className="entry-title">AI Safety Researcher — Safer AI (SPAR)</div>
          <div className="entry-meta">2025 – present · Remote</div>
          <p className="entry-desc">
            Conducting AI safety research through the SPAR (Supervised Program for Alignment
            Research) program, focused on empirical evaluation and robustness of ML systems.
          </p>
        </div>

        <div className="entry">
          <div className="entry-title">Software Engineering Intern — Massey Services</div>
          <div className="entry-meta">May 2025 – Aug 2025 · Orlando, FL</div>
          <p className="entry-desc">
            Built and deployed a full-stack customer referral rewards system (C# .NET, Angular, Azure)
            processing $20K+ in monthly referrals. Shipped fixes to a production app serving 10 000+
            daily users.
          </p>
        </div>

        <div className="entry">
          <div className="entry-title">Machine Learning Engineer — VantixAI</div>
          <div className="entry-meta">Jan 2025 – May 2025 · Remote</div>
          <p className="entry-desc">
            Developed a production computer vision model (90%+ accuracy). Built a full-stack
            research platform for 100+ users with NLP-powered note-taking.
          </p>
        </div>

        <div className="entry">
          <div className="entry-title">Sole Undergraduate Researcher — ESGI Lithuania (Telia Analytics)</div>
          <div className="entry-meta">Jun 2025 · Remote</div>
          <div className="project-img-wrap" style={{ marginTop: '12px', marginBottom: '16px', maxWidth: '400px' }}>
            <img src="/telia.jpeg" alt="ESGI Lithuania" className="project-img" />
          </div>
          <p className="entry-desc">
            Selected among 30+ PhD researchers. Applied LLMs and GPU compute to millions of
            telecom data points, improving customer retention modelling by 30%.
          </p>
        </div>

        <div className="entry">
          <div className="entry-title">Software Engineering Intern — MeroSiksha</div>
          <div className="entry-meta">Jul 2023 – Jul 2024 · Kathmandu, Nepal</div>
          <p className="entry-desc">
            Developed scalable REST APIs (Node.js) for 10 000+ active users and implemented
            an ML recommendation system improving engagement by 15%.
          </p>
        </div>
      </div>

      {/* Projects */}
      <div className="about-section">
        <p className="about-section-title">Selected Projects</p>

        <div className="entry">
          <div className="entry-title">Finlit <span style={{ fontWeight: 400, color: 'var(--text-3)' }}>— NSA AI Hackathon 2024 · $1 000 Winner</span></div>
          <p className="entry-desc">
            AI-powered financial literacy platform for immigrants with portfolio management and
            visa-compliant investing tools.
          </p>
          <div className="entry-tags">
            <span className="tag">React</span><span className="tag">Flask</span><span className="tag">ML</span>
          </div>
          <a href="https://finlit-sigma.vercel.app" target="_blank" rel="noopener noreferrer" className="project-link">Live demo →</a>
        </div>

        <div className="entry">
          <div className="entry-title">Zero Panic in Movement <span style={{ fontWeight: 400, color: 'var(--text-3)' }}>— KnightHacks ROS2 Challenge 2025 · $2 000 Winner</span></div>
          <p className="entry-desc">
            Autonomous robot swarm using ROS2 and YOLOv8 for emergency evacuation.
          </p>
          <div className="entry-tags">
            <span className="tag">ROS2</span><span className="tag">YOLOv8</span><span className="tag">Arduino</span>
          </div>
          <a href="https://devpost.com/software/zero-panic-in-movement-zpm" target="_blank" rel="noopener noreferrer" className="project-link">Devpost →</a>
        </div>

        <div className="entry">
          <div className="entry-title">CuraSyn+ <span style={{ fontWeight: 400, color: 'var(--text-3)' }}>— HackHarvard 2025</span></div>
          <p className="entry-desc">
            Real-time stroke detection using OpenCV and AI with multilingual doctor matching (6+ languages).
          </p>
          <div className="entry-tags">
            <span className="tag">React</span><span className="tag">OpenCV</span><span className="tag">Gemini AI</span>
          </div>
          <a href="https://curasyn.onrender.com" target="_blank" rel="noopener noreferrer" className="project-link">Live demo →</a>
        </div>
      </div>

      {/* Skills */}
      <div className="about-section">
        <p className="about-section-title">Skills</p>
        <div className="skills-group">
          <span className="skills-label">Languages: </span>
          <span className="skills-list">Python, Java, C++, C#, JavaScript, SQL, R, Go</span>
        </div>
        <div className="skills-group">
          <span className="skills-label">ML &amp; Research: </span>
          <span className="skills-list">TensorFlow, PyTorch, scikit-learn, OpenCV, NumPy, adversarial attacks, LLM evaluation</span>
        </div>
        <div className="skills-group">
          <span className="skills-label">Engineering: </span>
          <span className="skills-list">React, Flask, Node.js, .NET, Docker, AWS, Azure</span>
        </div>
      </div>

      {/* Contact */}
      <div className="about-section">
        <p className="about-section-title">Contact</p>
        <p>
          Open to discussing empirical safety research, adversarial ML, or PhD opportunities.
          Reach out at <a href="mailto:mkhanal@rollins.edu">mkhanal@rollins.edu</a>.
        </p>
      </div>

    </div>
  )
}

export default About
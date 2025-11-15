function About() {
  return (
    <div className="about-content">
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '40px', marginBottom: '50px', flexWrap: 'wrap' }}>
        <img 
          src="/profile.jpeg" 
          alt="Madhav Khanal"
          style={{
            width: '200px',
            height: '200px',
            borderRadius: '50%',
            objectFit: 'cover',
            border: '1px solid var(--border)'
          }}
        />
        <div style={{ flex: 1, minWidth: '300px' }}>
          <h1 style={{ fontSize: '48px', marginBottom: '10px', fontWeight: '700' }}>
            Madhav Khanal
          </h1>
          <p style={{ fontSize: '20px', color: 'var(--text-secondary)', marginBottom: '25px' }}>
            CS and Math Double Major | Alfond Scholar at Rollins College
          </p>
          
          <div style={{ display: 'flex', gap: '15px', flexWrap: 'wrap', marginTop: '20px' }}>
            <a 
              href="https://github.com/actionproject-madhav" 
              target="_blank" 
              rel="noopener noreferrer"
              style={{
                padding: '10px 20px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                transition: 'background-color 0.2s'
              }}
            >
              GitHub
            </a>
            <a 
              href="https://linkedin.com/in/madhav-khanal3145/" 
              target="_blank" 
              rel="noopener noreferrer"
              style={{
                padding: '10px 20px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                transition: 'background-color 0.2s'
              }}
            >
              LinkedIn
            </a>
            <a 
              href="mailto:mkhanal@rollins.edu"
              style={{
                padding: '10px 20px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                transition: 'background-color 0.2s'
              }}
            >
              Email
            </a>
          </div>
        </div>
      </div>

      {/* SPLINE PLACEHOLDER - Add interactive 3D animation here */}
      <div style={{ 
        width: '100%', 
        height: '400px', 
        backgroundColor: 'var(--bg-secondary)', 
        borderRadius: '12px',
        marginBottom: '60px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        border: '1px solid var(--border)'
      }}>
        <p style={{ color: 'var(--text-muted)' }}>
          [Spline 3D Animation Placeholder - Suggested: Floating geometric shapes or abstract tech visualization]
        </p>
      </div>

      <section style={{ marginBottom: '60px' }}>
        <h2 style={{ fontSize: '32px', marginBottom: '20px', fontWeight: '600' }}>Background</h2>
        <p style={{ fontSize: '18px', lineHeight: '1.8', color: 'var(--text-secondary)', marginBottom: '20px' }}>
          Full-ride Alfond Scholar at Rollins College pursuing a double major in Computer Science and Mathematics with a minor in Data Analytics. First-generation college student maintaining a 4.0 GPA while building production systems and winning hackathons.
        </p>
        <p style={{ fontSize: '18px', lineHeight: '1.8', color: 'var(--text-secondary)' }}>
          Former International Physics Olympiad national team member for Nepal. Currently working as a Software Engineering Intern at Massey Services, building systems that serve thousands of daily users.
        </p>
      </section>

      <section style={{ marginBottom: '60px' }}>
        <h2 style={{ fontSize: '32px', marginBottom: '20px', fontWeight: '600' }}>Experience</h2>
        
        <div style={{ marginBottom: '30px' }}>
          <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '8px' }}>
            Software Engineering Intern at Massey Services
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            May 2025 - Aug 2025 | Orlando, FL
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Built and deployed a full-stack customer referral rewards system using C# .NET, Angular, and Azure that processes over $20K in monthly referrals from 1000+ customers, eliminating 10+ hours of weekly manual work. Shipped critical bug fixes to production application serving 10,000+ daily active users.
          </p>
        </div>

        <div style={{ marginBottom: '30px' }}>
          <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '8px' }}>
            Machine Learning Engineer at VantixAI
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            Jan 2025 - May 2025 | Remote
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Developed production-ready computer vision model achieving 90%+ accuracy using Python and TensorFlow. Built full-stack research platform serving 100+ users with React frontend and Python backend, implementing intelligent note-taking with natural language processing.
          </p>
        </div>

        <div style={{ marginBottom: '30px' }}>
          <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '8px' }}>
            Software Engineering Intern at MeroSiksha
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            Jul 2023 - Jul 2024 | Kathmandu, Nepal
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Developed scalable REST APIs using Node.js to handle data from 10,000+ active users. Implemented machine learning recommendation system achieving 15% improvement in user engagement.
          </p>
        </div>
      </section>

      {/* PROJECT SHOWCASE IMAGE PLACEHOLDER */}
      <div style={{ 
        width: '100%', 
        height: '300px', 
        backgroundColor: 'var(--bg-secondary)', 
        borderRadius: '12px',
        marginBottom: '60px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        border: '1px solid var(--border)'
      }}>
        <p style={{ color: 'var(--text-muted)' }}>
          [Image Placeholder - Suggested: Collage of your hackathon projects or code screenshots]
        </p>
      </div>

      <section style={{ marginBottom: '60px' }}>
        <h2 style={{ fontSize: '32px', marginBottom: '20px', fontWeight: '600' }}>Notable Projects</h2>
        
        <div style={{ marginBottom: '30px' }}>
          <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '8px' }}>
            Telia Analytics - European Study Group with Industry
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            Jun 2025 | ESGI Palanga, Lithuania
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Selected as the sole undergraduate among 30+ PhD researchers from Oxford and global universities. Processed millions of telecom data points using LLMs and GPU computing, developing ML models that increased customer retention by 30%.
          </p>
        </div>

        <div style={{ marginBottom: '30px' }}>
          <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '8px' }}>
            Finlit - NSA AI Hackathon Winner
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            Aug 2024 | Won $1000 + Momo VC mentorship
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Built full-stack AI-powered financial literacy platform for immigrants with portfolio management, visa-compliant investing tools, and gamified education modules using React, Flask, and machine learning.
          </p>
        </div>

        <div style={{ marginBottom: '30px' }}>
          <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '8px' }}>
            Zero Panic in Movement - KnightHacks Winner
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            Oct 2025 | Won $2000 at ROS2 Autonomy Challenge
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Developed autonomous robot swarm using ROS2, Arduino, and YOLOv8 computer vision for emergency evacuation. Implemented swarm intelligence with A* pathfinding to detect humans and obstacles, dynamically mapping optimal exit routes.
          </p>
        </div>
      </section>

      <section style={{ marginBottom: '60px' }}>
        <h2 style={{ fontSize: '32px', marginBottom: '20px', fontWeight: '600' }}>Technical Skills</h2>
        
        <div style={{ marginBottom: '20px' }}>
          <h3 style={{ fontSize: '18px', fontWeight: '600', marginBottom: '10px', color: 'var(--text-primary)' }}>
            Languages
          </h3>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Java, JavaScript, Python, C++, C#, C, Go, HTML/CSS, SQL (PostgreSQL, SQLite), R
          </p>
        </div>

        <div style={{ marginBottom: '20px' }}>
          <h3 style={{ fontSize: '18px', fontWeight: '600', marginBottom: '10px', color: 'var(--text-primary)' }}>
            Frameworks & Tools
          </h3>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            React, Node.js, Angular, Flask, .NET, FastAPI, Git, Docker, AWS, Azure, Linux, Agile, CI/CD, RESTful APIs
          </p>
        </div>

        <div>
          <h3 style={{ fontSize: '18px', fontWeight: '600', marginBottom: '10px', color: 'var(--text-primary)' }}>
            ML & Data Science
          </h3>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            TensorFlow, PyTorch, scikit-learn, OpenCV, NumPy, Matplotlib
          </p>
        </div>
      </section>

      <section>
        <h2 style={{ fontSize: '32px', marginBottom: '20px', fontWeight: '600' }}>Get in Touch</h2>
        <p style={{ fontSize: '18px', lineHeight: '1.8', color: 'var(--text-secondary)' }}>
          Always open to discussing interesting problems, collaborating on projects, or connecting with fellow developers and researchers. Reach out through any of the platforms above.
        </p>
      </section>
    </div>
  )
}

export default About
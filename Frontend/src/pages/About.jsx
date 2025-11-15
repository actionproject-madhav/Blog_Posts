import Spline from '@splinetool/react-spline'

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
              onMouseEnter={(e) => e.target.style.backgroundColor = 'var(--bg-secondary)'}
              onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
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
              onMouseEnter={(e) => e.target.style.backgroundColor = 'var(--bg-secondary)'}
              onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
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
              onMouseEnter={(e) => e.target.style.backgroundColor = 'var(--bg-secondary)'}
              onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
            >
              Email
            </a>
            <a 
              href="/resume.pdf"
              download
              style={{
                padding: '10px 20px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                transition: 'background-color 0.2s',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '6px'
              }}
              onMouseEnter={(e) => e.target.style.backgroundColor = 'var(--bg-secondary)'}
              onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
            >
              📄 Resume
            </a>
          </div>
        </div>
      </div>

      {/* Spline 3D Animation */}
      <div style={{ 
        position: 'relative',
        width: '100%', 
        height: '500px', 
        borderRadius: '12px',
        marginBottom: '60px',
        overflow: 'hidden',
        border: '1px solid var(--border)'
      }}>
        <Spline
          scene="https://prod.spline.design/Anob6XCn921GlqBo/scene.splinecode"
        />
        {/* Watermark overlay - darken/blur bottom right corner */}
        <div style={{
          position: 'absolute',
          bottom: 0,
          right: 0,
          width: '200px',
          height: '80px',
          background: 'linear-gradient(to top right, var(--bg-primary) 0%, var(--bg-primary) 50%, transparent 100%)',
          zIndex: 3,
          pointerEvents: 'none',
          backdropFilter: 'blur(8px)',
          WebkitBackdropFilter: 'blur(8px)',
          borderRadius: '0 0 12px 0'
        }}></div>
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
            Business Analytics Intern at Massey Services
          </h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '15px', marginBottom: '12px' }}>
            May 2025 - Aug 2025 | Orlando, FL
          </p>
          <p style={{ fontSize: '16px', lineHeight: '1.7', color: 'var(--text-secondary)' }}>
            Analyzed operational datasets for 500+ locations using Python and SQL, developing data-driven solutions. Built automated reporting workflows using Python, reducing data processing time by 60% through efficient algorithms.
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

      <section style={{ marginBottom: '60px' }}>
        <h2 style={{ fontSize: '32px', marginBottom: '30px', fontWeight: '600' }}>Featured Projects</h2>
        
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', 
          gap: '30px',
          marginBottom: '40px'
        }}>
          {/* Finlit Project */}
          <a 
            href="https://finlit-uyv5.onrender.com"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              textDecoration: 'none',
              color: 'inherit',
              display: 'block',
              backgroundColor: 'var(--bg-secondary)',
              borderRadius: '12px',
              overflow: 'hidden',
              border: '1px solid var(--border)',
              transition: 'transform 0.2s, box-shadow 0.2s',
              cursor: 'pointer'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'translateY(-4px)'
              e.currentTarget.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.15)'
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'translateY(0)'
              e.currentTarget.style.boxShadow = 'none'
            }}
          >
            <div style={{ 
              width: '100%', 
              height: '200px', 
              backgroundColor: 'var(--bg-secondary)',
              backgroundImage: 'url(/projects/finlit.jpg)',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              position: 'relative'
            }}>
              <div style={{
                position: 'absolute',
                bottom: '8px',
                right: '8px',
                fontSize: '11px',
                color: 'var(--text-muted)',
                backgroundColor: 'rgba(0, 0, 0, 0.6)',
                padding: '4px 8px',
                borderRadius: '4px'
              }}>
                Add: /public/projects/finlit.jpg
              </div>
            </div>
            <div style={{ padding: '24px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '12px' }}>
                <h3 style={{ fontSize: '20px', fontWeight: '600', margin: 0, color: 'var(--text-primary)' }}>
                  Finlit
                </h3>
                <span style={{ 
                  fontSize: '12px', 
                  padding: '4px 10px',
                  backgroundColor: 'var(--accent)',
                  color: 'var(--bg-primary)',
                  borderRadius: '12px',
                  fontWeight: '600'
                }}>
                  $1000 Winner
                </span>
              </div>
              <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '12px' }}>
                NSA AI Hackathon 2024 | Momo VC Mentorship
              </p>
              <p style={{ fontSize: '15px', lineHeight: '1.6', color: 'var(--text-secondary)', marginBottom: '16px' }}>
                AI-powered financial literacy platform for immigrants with portfolio management and visa-compliant investing tools.
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '12px' }}>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>React</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>Flask</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>ML</span>
              </div>
              <div style={{ fontSize: '14px', color: 'var(--accent)', fontWeight: '500' }}>
                View Demo →
              </div>
            </div>
          </a>

          {/* Zero Panic Project */}
          <a 
            href="https://devpost.com/software/zero-panic-in-movement-zpm"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              textDecoration: 'none',
              color: 'inherit',
              display: 'block',
              backgroundColor: 'var(--bg-secondary)',
              borderRadius: '12px',
              overflow: 'hidden',
              border: '1px solid var(--border)',
              transition: 'transform 0.2s, box-shadow 0.2s',
              cursor: 'pointer'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'translateY(-4px)'
              e.currentTarget.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.15)'
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'translateY(0)'
              e.currentTarget.style.boxShadow = 'none'
            }}
          >
      <div style={{ 
        width: '100%', 
              height: '200px', 
              backgroundColor: 'var(--bg-secondary)',
              backgroundImage: 'url(/projects/zpm.jpg)',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              position: 'relative'
            }}>
              <div style={{
                position: 'absolute',
                bottom: '8px',
                right: '8px',
                fontSize: '11px',
                color: 'var(--text-muted)',
                backgroundColor: 'rgba(0, 0, 0, 0.6)',
                padding: '4px 8px',
                borderRadius: '4px'
              }}>
                Add: /public/projects/zpm.jpg
              </div>
            </div>
            <div style={{ padding: '24px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '12px' }}>
                <h3 style={{ fontSize: '20px', fontWeight: '600', margin: 0, color: 'var(--text-primary)' }}>
                  Zero Panic in Movement
                </h3>
                <span style={{ 
                  fontSize: '12px', 
                  padding: '4px 10px',
                  backgroundColor: 'var(--accent)',
                  color: 'var(--bg-primary)',
                  borderRadius: '12px',
                  fontWeight: '600'
                }}>
                  $2000 Winner
                </span>
              </div>
              <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '12px' }}>
                KnightHacks ROS2 Challenge 2025
              </p>
              <p style={{ fontSize: '15px', lineHeight: '1.6', color: 'var(--text-secondary)', marginBottom: '16px' }}>
                Autonomous robot swarm using ROS2 and YOLOv8 for emergency evacuation with swarm intelligence.
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '12px' }}>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>ROS2</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>YOLOv8</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>Arduino</span>
              </div>
              <div style={{ fontSize: '14px', color: 'var(--accent)', fontWeight: '500' }}>
                View Demo →
              </div>
            </div>
          </a>

          {/* CuraSyn Project */}
          <a 
            href="https://curasyn.onrender.com"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              textDecoration: 'none',
              color: 'inherit',
              display: 'block',
        backgroundColor: 'var(--bg-secondary)', 
        borderRadius: '12px',
              overflow: 'hidden',
              border: '1px solid var(--border)',
              transition: 'transform 0.2s, box-shadow 0.2s',
              cursor: 'pointer'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'translateY(-4px)'
              e.currentTarget.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.15)'
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'translateY(0)'
              e.currentTarget.style.boxShadow = 'none'
            }}
          >
            <div style={{ 
              width: '100%', 
              height: '200px', 
              backgroundColor: 'var(--bg-secondary)',
              backgroundImage: 'url(/projects/curasyn.jpg)',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              position: 'relative'
            }}>
              <div style={{
                position: 'absolute',
                bottom: '8px',
                right: '8px',
                fontSize: '11px',
                color: 'var(--text-muted)',
                backgroundColor: 'rgba(0, 0, 0, 0.6)',
                padding: '4px 8px',
                borderRadius: '4px'
              }}>
                Add: /public/projects/curasyn.jpg
              </div>
      </div>
            <div style={{ padding: '24px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '12px' }}>
                <h3 style={{ fontSize: '20px', fontWeight: '600', margin: 0, color: 'var(--text-primary)' }}>
                  CuraSyn+
          </h3>
                <span style={{ 
                  fontSize: '12px', 
                  padding: '4px 10px',
                  backgroundColor: 'var(--bg-primary)',
                  color: 'var(--text-primary)',
                  borderRadius: '12px',
                  border: '1px solid var(--border)',
                  fontWeight: '600'
                }}>
                  HackHarvard 2025
                </span>
              </div>
              <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '12px' }}>
                Healthcare Platform | WCAG 2.1 AA Compliant
              </p>
              <p style={{ fontSize: '15px', lineHeight: '1.6', color: 'var(--text-secondary)', marginBottom: '16px' }}>
                Real-time stroke detection using OpenCV and AI with multilingual doctor matching (6+ languages).
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '12px' }}>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>React</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>OpenCV</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>Gemini AI</span>
              </div>
              <div style={{ fontSize: '14px', color: 'var(--accent)', fontWeight: '500' }}>
                View Demo →
              </div>
        </div>
          </a>

          {/* Telia Analytics Project */}
          <a 
            href="#"
            style={{
              textDecoration: 'none',
              color: 'inherit',
              display: 'block',
              backgroundColor: 'var(--bg-secondary)',
              borderRadius: '12px',
              overflow: 'hidden',
              border: '1px solid var(--border)',
              transition: 'transform 0.2s, box-shadow 0.2s',
              cursor: 'pointer'
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'translateY(-4px)'
              e.currentTarget.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.15)'
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'translateY(0)'
              e.currentTarget.style.boxShadow = 'none'
            }}
          >
            <div style={{ 
              width: '100%', 
              height: '200px', 
              backgroundColor: 'var(--bg-secondary)',
              backgroundImage: 'url(/projects/telia.jpg)',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              position: 'relative'
            }}>
              <div style={{
                position: 'absolute',
                bottom: '8px',
                right: '8px',
                fontSize: '11px',
                color: 'var(--text-muted)',
                backgroundColor: 'rgba(0, 0, 0, 0.6)',
                padding: '4px 8px',
                borderRadius: '4px'
              }}>
                Add: /public/projects/telia.jpg
              </div>
            </div>
            <div style={{ padding: '24px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '12px' }}>
                <h3 style={{ fontSize: '20px', fontWeight: '600', margin: 0, color: 'var(--text-primary)' }}>
                  Telia Analytics
          </h3>
                <span style={{ 
                  fontSize: '12px', 
                  padding: '4px 10px',
                  backgroundColor: 'var(--bg-primary)',
                  color: 'var(--text-primary)',
                  borderRadius: '12px',
                  border: '1px solid var(--border)',
                  fontWeight: '600'
                }}>
                  ESGI Lithuania
                </span>
              </div>
              <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '12px' }}>
                Jun 2025 | Sole Undergraduate Selected
              </p>
              <p style={{ fontSize: '15px', lineHeight: '1.6', color: 'var(--text-secondary)', marginBottom: '16px' }}>
                Processed millions of telecom data points using LLMs and GPU, increasing customer retention by 30% with ML models.
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '12px' }}>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>Python</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>LLM</span>
                <span style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: 'var(--bg-primary)', borderRadius: '4px', color: 'var(--text-secondary)' }}>GPU</span>
              </div>
              <div style={{ fontSize: '14px', color: 'var(--text-muted)', fontWeight: '500' }}>
                Research Project
              </div>
        </div>
          </a>
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
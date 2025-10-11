function Resume() {
    return (
      <div className="resume-content">
        <div style={{ textAlign: 'center', marginBottom: '60px' }}>
          <h1 style={{ fontSize: '48px', marginBottom: '10px', fontWeight: '700' }}>
            Madhav Khanal
          </h1>
          <p style={{ fontSize: '20px', color: 'var(--text-secondary)', marginBottom: '30px' }}>
            Computer Science Student | Competitive Programmer | Math Enthusiast
          </p>
          
          <div style={{ display: 'flex', gap: '15px', justifyContent: 'center', flexWrap: 'wrap' }}>
            <a 
              href="https://github.com/actionproject-madhav" 
              target="_blank" 
              rel="noopener noreferrer"
              style={{
                padding: '12px 24px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                fontSize: '15px',
                transition: 'all 0.2s',
                display: 'inline-block'
              }}
            >
              GitHub
            </a>
            <a 
              href="https://www.linkedin.com/in/madhav-khanal3145/" 
              target="_blank" 
              rel="noopener noreferrer"
              style={{
                padding: '12px 24px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                fontSize: '15px',
                transition: 'all 0.2s',
                display: 'inline-block'
              }}
            >
              LinkedIn
            </a>
            
           
            <a 
              href="mailto:mkhanal@rollins.edu"
              style={{
                padding: '12px 24px',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                textDecoration: 'none',
                color: 'var(--text-primary)',
                fontSize: '15px',
                transition: 'all 0.2s',
                display: 'inline-block'
              }}
            >
              Email
            </a>
          </div>
        </div>
  
        <div style={{ maxWidth: '650px', margin: '0 auto' }}>
          <p style={{ fontSize: '18px', lineHeight: '1.8', marginBottom: '30px', textAlign: 'center' }}>
            I'm an undergraduate  computer science and mathematics double major passionate about algorithms, mathematics, machine learning, chess, 
            and building things that solve real problems. I love exploring elegant solutions and 
            sharing what I learn through writing and visualizations.
          </p>
  
    
  
          <h2 style={{ fontSize: '28px', marginTop: '40px', marginBottom: '20px' }}>
            Get in Touch
          </h2>
          <p>
            I'm always open to connecting with fellow learners, discussing interesting problems, 
            or collaborating on projects. Feel free to reach out through any of the platforms above!
          </p>
        </div>
      </div>
    )
  }
  
  export default Resume
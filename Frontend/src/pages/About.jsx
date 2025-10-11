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
              Undergrad Math and CS Double Major | Interested in Algorithms, Machine Learning, Puzzles, and Problem Solving
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
              </a>            </div>
          </div>
        </div>
      </div>
    );
  }
  
  export default About;
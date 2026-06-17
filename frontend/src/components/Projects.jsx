export default function Projects({ projects }) {
  return (
    <section id="portfolio" className="section projects">
      <div className="container">
        <h2 className="section__title">
          Latest <span className="highlight">Projects</span>
        </h2>
        <div className="projects__grid">
          {projects.map((project) => (
            <div key={project.id} className="project-card">
              <div className="project-card__image">
                <div className="project-card__placeholder">
                  {project.title.charAt(0)}
                </div>
                {project.status === 'pending' && (
                  <span className="project-card__badge">Under Development</span>
                )}
              </div>
              <div className="project-card__body">
                <h3>{project.title}</h3>
                <p>{project.description}</p>
                <div className="project-card__links">
                  {project.project_url && project.project_url !== '#' && (
                    <a href={project.project_url} target="_blank" rel="noreferrer" className="btn btn--sm btn--primary">
                      View Live
                    </a>
                  )}
                  {project.github_url && (
                    <a href={project.github_url} target="_blank" rel="noreferrer" className="btn btn--sm btn--outline">
                      GitHub
                    </a>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

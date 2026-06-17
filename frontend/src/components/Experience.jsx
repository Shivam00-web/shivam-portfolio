export default function Experience({ experience }) {
  return (
    <section id="experience" className="section experience">
      <div className="container">
        <h2 className="section__title">
          My <span className="highlight">Experience</span>
        </h2>
        <div className="experience__timeline">
          {experience.map((item, index) => (
            <div key={item.id} className="experience__item">
              <div className="experience__marker">
                <span className="experience__dot" />
                {index < experience.length - 1 && <span className="experience__line" />}
              </div>
              <div className="experience__card">
                <div className="experience__header">
                  <div>
                    <h3>{item.role}</h3>
                    <p className="experience__company">{item.company}</p>
                  </div>
                  <div className="experience__meta">
                    <span className="experience__date">
                      {item.start_date} — {item.is_current ? 'Present' : item.end_date}
                    </span>
                    {item.location && (
                      <span className="experience__location">{item.location}</span>
                    )}
                  </div>
                </div>
                <p className="experience__desc">{item.description}</p>
                {item.is_current && (
                  <span className="experience__badge">Current</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

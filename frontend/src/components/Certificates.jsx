import DisplayImage from './DisplayImage';

export default function Certificates({ certificates }) {
  return (
    <section id="certificates" className="section certificates">
      <div className="container">
        <h2 className="section__title">
          My <span className="highlight">Certificates</span>
        </h2>
        <div className="certificates__grid">
          {certificates.map((cert) => (
            <div key={cert.id} className="cert-card">
              <div className="cert-card__icon">
                <DisplayImage
                  src={cert.display_image}
                  alt={cert.title}
                  className="cert-card__logo"
                  placeholder="📜"
                />
              </div>
              <h3>{cert.title}</h3>
              {cert.description && <p>{cert.description}</p>}
              <div className="cert-card__actions">
                <button className="btn btn--sm btn--outline">Read More</button>
                {cert.download_url && (
                  <a href={cert.download_url} className="btn btn--sm btn--primary" download>
                    Download
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

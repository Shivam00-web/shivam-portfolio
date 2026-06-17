import { useState } from 'react';

export default function About({ profile }) {
  const [expanded, setExpanded] = useState(false);

  const shortBio = profile.bio.slice(0, 200) + '...';

  return (
    <section id="about" className="section about">
      <div className="container">
        <h2 className="section__title">
          About <span className="highlight">Me</span>
        </h2>
        <div className="about__grid">
          <div className="about__image">
            <div className="about__avatar">
              {profile.profile_image ? (
                <img src={profile.profile_image} alt={profile.name} />
              ) : (
                <span>SV</span>
              )}
            </div>
          </div>
          <div className="about__content">
            <h3>{profile.title}!</h3>
            <p className="about__tagline">{profile.tagline}</p>
            <p>{expanded ? profile.bio : shortBio}</p>
            <button
              className="btn btn--outline"
              onClick={() => setExpanded(!expanded)}
            >
              {expanded ? 'Read Less' : 'Read More'}
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

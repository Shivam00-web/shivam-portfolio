import { useTypewriter } from '../hooks/useTypewriter';

export default function Hero({ profile }) {
  const typedRole = useTypewriter(profile.roles, 120, 1800);

  return (
    <section id="home" className="hero">
      <div className="container hero__inner">
        <div className="hero__content">
          <p className="hero__greeting">Hello, It&apos;s Me</p>
          <h1 className="hero__name">{profile.name}</h1>
          <h2 className="hero__role">
            And I&apos;m a <span className="highlight">{typedRole}</span>
            <span className="cursor">|</span>
          </h2>
          <p className="hero__bio">{profile.bio}</p>
          <div className="hero__actions">
            <a href={profile.cv_url} className="btn btn--primary" download>
              Download CV
            </a>
            <div className="hero__social">
              <a href={profile.social.github} target="_blank" rel="noreferrer" aria-label="GitHub">
                <i className="icon-github" />
              </a>
              <a href={profile.social.linkedin} target="_blank" rel="noreferrer" aria-label="LinkedIn">
                <i className="icon-linkedin" />
              </a>
              <a href={`mailto:${profile.social.email}`} aria-label="Email">
                <i className="icon-mail" />
              </a>
            </div>
          </div>
        </div>
        <div className="hero__image">
          <div className="hero__image-ring">
            <div className="hero__avatar">
              {profile.profile_image ? (
                <img src={profile.profile_image} alt={profile.name} />
              ) : (
                <span>SV</span>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

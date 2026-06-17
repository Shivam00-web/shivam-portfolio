import { useState } from 'react';
import DisplayImage from './DisplayImage';

export default function Skills({ skills }) {
  const [activeSkill, setActiveSkill] = useState(null);

  return (
    <section id="skills" className="section skills">
      <div className="container">
        <h2 className="section__title">
          My <span className="highlight">Skills</span>
        </h2>
        <div className="skills__grid">
          {skills.map((skill) => (
            <div
              key={skill.id}
              className={`skill-card ${activeSkill === skill.id ? 'active' : ''}`}
              onClick={() => setActiveSkill(activeSkill === skill.id ? null : skill.id)}
            >
              <div className="skill-card__icon">
                <DisplayImage
                  src={skill.display_image}
                  alt={skill.title}
                  className="skill-card__logo"
                  placeholder="⚡"
                />
              </div>
              <h3>{skill.title}</h3>
              <p className="skill-card__desc">{skill.description}</p>
              <button className="skill-card__btn">Read More</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

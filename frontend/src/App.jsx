import { useEffect, useState } from 'react';
import { fetchPortfolio } from './api/api';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Skills from './components/Skills';
import Certificates from './components/Certificates';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './index.css';

const FALLBACK_DATA = {
  profile: {
    name: 'Shivam Verma',
    title: 'IOT ENGINEER | SOFTWARE DEVELOPER',
    tagline: 'Passionate Learner | Creative Thinker',
    bio: "I'm a motivated and enthusiastic IOT ENGINEER AND SOFTWARE DEVELOPER Developer with a strong interest in web design, IoT projects, and creative problem solving. I recently completed several hands-on projects like an Amazon and Flipkart website clone, a Music Player web app, and a Student Management System. I enjoy building responsive and user-friendly websites using HTML, CSS, JavaScript, and Tailwind CSS, and have also explored backend technologies like Django and MySQL.",
    roles: ['Frontend Developer', 'Web Designer', 'IoT Enthusiast', 'Creative Thinker'],
    cv_url: '#',
    social: {
      github: 'https://github.com/shivam00-web',
      linkedin: 'https://www.linkedin.com/in/shivam9528/',
      email: 'sv873234@gmail.com',
    },
    profile_image: null,
  },
  skills: [],
  certificates: [],
  experience: [],
  projects: [],
};

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchPortfolio()
      .then(setData)
      .catch(() => setData(FALLBACK_DATA))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="loader">
        <div className="loader__spinner" />
        <p>Loading Portfolio...</p>
      </div>
    );
  }

  const { profile, skills, certificates, experience, projects } = data;

  return (
    <>
      <Navbar />
      <main>
        <Hero profile={profile} />
        <About profile={profile} />
        {experience.length > 0 && <Experience experience={experience} />}
        {skills.length > 0 && <Skills skills={skills} />}
        {certificates.length > 0 && <Certificates certificates={certificates} />}
        {projects.length > 0 && <Projects projects={projects} />}
        <Contact />
      </main>
      <Footer />
    </>
  );
}

export default App;

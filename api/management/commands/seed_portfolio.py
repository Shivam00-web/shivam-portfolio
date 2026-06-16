from django.core.management.base import BaseCommand

from api.models import Certificate, Experience, Project, Skill


class Command(BaseCommand):
    help = 'Seed portfolio database with initial data'

    def handle(self, *args, **options):
        Skill.objects.all().delete()
        Certificate.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()

        skills = [
            ('Web Development', 'I have created a Website called MGV ARTWORKS to sell my artworks.', '🌐', 1),
            ('Graphic Design', 'I have designed many Logos for personal websites and clients.', '🎨', 2),
            ('IoT Enthusiast', 'Passionate about creating smart solutions by connecting hardware with software.', '⚡', 3),
            ('HTML', 'Structures content on the web.', '📄', 4),
            ('CSS', 'Styles and designs web pages by controlling layout, colors, and fonts.', '🎨', 5),
            ('JavaScript', 'Scripting language used to build dynamic and interactive websites.', '⚙️', 6),
            ('Tailwind CSS', 'Utility-first CSS framework for building custom user interfaces.', '💨', 7),
            ('Python', 'Powerful and versatile programming language for web, AI, data, and automation.', '🐍', 8),
            ('DBMS', 'Database systems for managing structured data efficiently.', '🗄️', 9),
            ('Embedded Systems', 'Developing hardware-software integrated systems using MCUs and real-time logic.', '🔧', 10),
            ('Arduino Uno', 'Building smart hardware projects using Arduino ESP32 microcontroller boards.', '📟', 11),
            ('Microcontroller 8051', 'Working with 8051 architecture for embedded applications and low-level programming.', '💾', 12),
            ('Computer Networking', 'Building and understanding communication between connected systems and devices.', '🌐', 13),
            ('Django Framework', 'A high-level Python web framework for building secure and scalable web apps fast.', 'Dj', 14),
        ]

        for title, desc, icon, order in skills:
            Skill.objects.create(title=title, description=desc, icon=icon, order=order)

        certificates = [
            ('HTML Certificate', 'Certified in HTML fundamentals and semantic markup.', '📜', '', 1),
            ('Graphic Design Certificate', 'Certified in graphic design principles and tools.', '🎨', '', 2),
            ('Web Development Certificate', 'Certified in full-stack web development.', '🌐', '', 3),
            ('IoT Enthusiast Certificate', 'Certified in IoT concepts and implementations.', '⚡', '', 4),
            ('CSS Certificate', 'Certified in CSS styling and responsive design.', '🎨', '', 5),
            ('JavaScript Certificate', 'Certified in JavaScript programming.', '⚙️', '', 6),
            ('Tailwind CSS Certificate', 'Certified in Tailwind CSS framework.', '💨', '', 7),
            ('Python Certificate', 'Certified in Python programming.', '🐍', '', 8),
            ('DBMS Certificate', 'Certified in database management systems.', '🗄️', '', 9),
            ('Embedded Systems Certificate', 'Certified in embedded systems development.', '🔧', '', 10),
            ('Arduino Uno Certificate', 'Certified in Arduino development.', '📟', '', 11),
            ('Microcontroller 8051 Certificate', 'Certified in 8051 microcontroller programming.', '💾', '', 12),
            ('Computer Networking Certificate', 'Certified in computer networking fundamentals.', '🌐', '', 13),
            ('Django Framework Certificate', 'Certified in Django web framework.', 'Dj', '', 14),
        ]

        for title, desc, icon, url, order in certificates:
            Certificate.objects.create(
                title=title, description=desc, icon=icon,
                download_url=url, order=order,
            )

        experiences = [
            (
                'Frontend Developer (Fresher)', 'Personal Projects',
                'Remote', '2024', 'Present', True,
                'Built responsive websites including e-commerce clones, a music player web app, '
                'and a full-stack portfolio using React, HTML, CSS, JavaScript, and Django.',
                1,
            ),
            (
                'Freelance Web Developer', 'Self Employed',
                'India', '2023', '2024', False,
                'Designed and developed client websites and logos. Created MGV ARTWORKS, '
                'a personal platform to showcase and sell digital artwork.',
                2,
            ),
            (
                'IoT Project Developer', 'Academic & Personal Projects',
                'India', '2022', 'Present', True,
                'Developed smart hardware solutions using Arduino ESP32, 8051 microcontrollers, '
                'and embedded C/C++ for automation and sensor-based systems.',
                3,
            ),
            (
                'Web Development Trainee', 'Online Learning Programs',
                'Remote', '2023', '2024', False,
                'Completed hands-on training in HTML, CSS, JavaScript, Tailwind CSS, Python, '
                'Django, and database management through project-based learning.',
                4,
            ),
        ]

        for role, company, location, start, end, current, desc, order in experiences:
            Experience.objects.create(
                role=role, company=company, location=location,
                start_date=start, end_date=end, is_current=current,
                description=desc, order=order,
            )

        projects = [
            (
                'MGV ARTWORKS', 'My own personal artwork website.',
                '', '#', '', 'completed', 1,
            ),
            (
                'Full Stack Portfolio', 'A modern portfolio built with React and Django REST API.',
                '', '#', '', 'completed', 2,
            ),
            (
                'Artisans Avenue', 'An E-Commerce website to sell artworks.',
                '', '#', '', 'completed', 3,
            ),
            (
                'Amazon Clone', 'A responsive e-commerce website clone built with HTML, CSS, and JavaScript.',
                '', '#', '', 'pending', 4,
            ),
            (
                'Student Management System', 'A full-stack application for managing student records.',
                '', '#', '', 'pending', 5,
            ),
        ]

        for title, desc, img, url, github, status, order in projects:
            Project.objects.create(
                title=title, description=desc, image_url=img,
                project_url=url, github_url=github, status=status, order=order,
            )

        self.stdout.write(self.style.SUCCESS('Portfolio data seeded successfully!'))

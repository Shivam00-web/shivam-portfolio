# Shivam Portfolio

A modern full-stack portfolio website built with **React**, **HTML/CSS/JS**, and **Django REST Framework**.

## Project Location

Rename the project folder to `shivam-portfolio` in File Explorer (close Cursor first):

```
e:\django-web\age and gender  →  e:\django-web\shivam-portfolio
```

Then reopen the project from `e:\django-web\shivam-portfolio`.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19, Vite, HTML, CSS, JavaScript |
| Backend | Django 5, Django REST Framework |
| Database | SQLite |
| API | RESTful JSON API |

## Project Structure

```
├── backend/          # Django REST API
│   ├── api/          # Portfolio models, views, serializers
│   └── portfolio_backend/  # Django settings
└── frontend/         # React SPA
    └── src/
        ├── components/   # Navbar, Hero, About, Skills, etc.
        ├── api/            # API client
        └── hooks/          # Custom React hooks
```

## Features

- Animated hero with typewriter effect
- About, Experience, Skills, Certificates, and Projects sections
- Contact form backed by Django API
- Fully responsive design
- Dark theme with modern UI
- Admin panel to manage portfolio content

## Getting Started

### 1. Backend (Django)

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_portfolio
python manage.py runserver
```

API runs at `http://127.0.0.1:8000/api/`

### 2. Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

> **Note:** If you renamed the folder, use `cd e:\django-web\shivam-portfolio\backend` and `...\frontend` instead.

### 3. Admin Panel

Create a superuser to manage content:

```bash
cd backend
python manage.py createsuperuser
```

Admin panel: `http://127.0.0.1:8000/admin/`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/portfolio/` | All portfolio data |
| GET | `/api/skills/` | Skills list |
| GET | `/api/certificates/` | Certificates list |
| GET | `/api/experience/` | Experience list |
| GET | `/api/projects/` | Projects list |
| POST | `/api/contact/` | Submit contact message |

## License

Copyright © 2025 by Shivam | All Rights Reserved

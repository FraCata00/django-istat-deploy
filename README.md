# 🚀 Django ISTAT Deployment

Production-ready deployment setup for the **Django ISTAT Italian Places** project.

---

## 📌 Overview

This repository contains the configuration and setup required to deploy the Django ISTAT backend in a production-like environment.

It focuses on:

- Containerization
- Environment configuration
- Deployment workflow

---

## 🧠 Tech Stack

- Docker
- Docker Compose
- PostgreSQL
- Django

---

## 🐳 Services

The system is composed of:

- **web** → Django application
- **db** → PostgreSQL database

---

## ⚙️ Setup & Run

```bash
git clone https://github.com/FraCata00/django-istat-deploy.git
cd django-istat-deploy

cp .env.example .env

docker-compose up --build
```

---

## 🔐 Environment Variables

Create a .env file:

```env
DEBUG=False
SECRET_KEY=your_secret_key
POSTGRES_DB=istat_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

---

## 📡 Application Access

- API: http://localhost:8000/comuni_italiani/
- Admin: http://localhost:8000/admin

---

>Main project: https://github.com/FraCata00/django-istat-italian-places

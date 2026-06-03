# FastAPI Social API

A RESTful social media backend API built with FastAPI.

This project allows users to register, authenticate using JWT tokens, create posts, vote on posts, and interact with a PostgreSQL database.

## Features

- User registration
- JWT Authentication
- Login system
- Create, update and delete posts
- Vote system
- Ownership protection
- PostgreSQL database
- SQLAlchemy ORM
- Alembic migrations
- CORS support
- Environment variable configuration

---

## Tech Stack

## 🛠️ Tech Stack

- 🐍 [Python](https://www.python.org/)
- ⚡ [FastAPI](https://fastapi.tiangolo.com/)
- 🐘 [PostgreSQL](https://www.postgresql.org/)
- 🗄️ [SQLAlchemy](https://www.sqlalchemy.org/)
- 🔄 [Alembic](https://alembic.sqlalchemy.org/)
- 🔐 JWT Authentication
- ✅ [Pydantic](https://docs.pydantic.dev/)
- 🚀 [Uvicorn](https://www.uvicorn.org/)
---

## Project Structure

```
FastAPI_Social_API/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── posts.py
│   │   ├── users.py
│   │   └── votes.py
│   │
│   ├── models.py
│   ├── schemas.py
│   ├── oauth2.py
│   ├── config.py
│   ├── utils.py
│   ├── database.py
│   └── main.py
│
├── alembic/
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/VladM-Sashev/FastAPI_Social_API.git
```

Go into project:

```bash
cd FastAPI_Social_API
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Authentication

Protected routes require JWT token:

```text
Authorization: Bearer <token>
```

---

## Future Improvements

- Comments system
- Docker support
- WebSockets
- Redis caching
- React frontend
- Testing

---

## Author

Vladimir Merdzhanov

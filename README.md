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

### 1. Clone the repository

```bash
git clone https://github.com/VladM-Sashev/FastAPI_Social_API.git
cd FastAPI_Social_API
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure the following variables:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi_2026
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure PostgreSQL is running and create the database before running migrations:

```sql
CREATE DATABASE fastapi_2026;
```

If you included a `.env.example` file in the repository, you can copy it with:

```bash
cp .env.example .env
```

Then update the values in `.env` with your local PostgreSQL credentials and secret key.


### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

### 7. Open API Documentation

```
http://127.0.0.1:8000/docs
```

## Database Migrations

This project uses Alembic for database version control.

To apply all migrations:

```bash
alembic upgrade head
```

To create a new migration:

```bash
alembic revision --autogenerate -m "migration description"
```

To apply the new migration:

```bash
alembic upgrade head
```


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

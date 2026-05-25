from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import posts, users, auth, votes

app = FastAPI(
    title="FastAPI Social API",
    description="A REST API for users, posts, authentication, and voting.",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)







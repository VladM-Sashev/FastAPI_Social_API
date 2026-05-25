from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Annotated


class PostCreate(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    owner: UserOut

    class Config:
        from_attributes = True


class PostOutWithVotes(BaseModel):
    Post: PostOut
    votes: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]


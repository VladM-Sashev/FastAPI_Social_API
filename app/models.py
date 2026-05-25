from sqlalchemy import Integer, Boolean, String, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .database import Base

class Post(Base):
    __tablename__="posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, server_default="True", nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    owner_id: Mapped[int] = mapped_column(Integer,ForeignKey("users.id", ondelete="CASCADE"), nullable=False )
    owner: Mapped["User"] = relationship(back_populates="posts")


class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    posts: Mapped[list["Post"]] = relationship(back_populates="owner")

class Vote(Base):
    __tablename__="votes"
    post_id: Mapped[int]=mapped_column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
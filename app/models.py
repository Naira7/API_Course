from tkinter import CASCADE
from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, true
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    user_id = Column(Integer, ForeignKey("Users.id", ondelete=CASCADE), nullable=False)
    user = relationship("User")


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))



class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("Users.id", ondelete=CASCADE), primary_key=True)
    post_id = Column(Integer, ForeignKey("Posts.id", ondelete=CASCADE), primary_key=True)


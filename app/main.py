
from operator import imod
from sre_constants import SUCCESS
from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker
from . import models
from . import schemas, utils, oauth2
from .Routers import post, user, auth, vote
from . import config
from fastapi.middleware.cors import CORSMiddleware


from .database import engine, SessionLocal, get_db

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#models.Base.metadata.create_all(bind=engine)



  


# my_posts = [{"title":"Some title", "content":"some content", "id":1}]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index(id):
#     for i,p in enumerate(my_posts):
#         if p["id"]==id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def root():
    return {'message': 'Hello World'}










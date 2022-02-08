
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime





class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
   

class UserLogin(BaseModel):
    email: EmailStr
    password: str   


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True 

class Post(BaseModel):
    title: str
    content: str
    published: bool = True 
  


class PostCreate(Post):
    pass



class PostResponse(Post):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponse

    class Config:
        orm_mode = True



class PostVoteBase(Post):
    id: int
    created_at: datetime
    user_id: int



class PostVoteResponse(BaseModel):
    Post:PostResponse
    votes:int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None



class Vote(BaseModel):
    post_id: int
    dir: int
    

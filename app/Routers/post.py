from .. import models
from .. import schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi.params import Body
from typing import List, Optional
from sqlalchemy import func

router = APIRouter(
    tags = ['Post']
)

@router.get('/posts/alchemy')
def test_get(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


#@router.get('/posts', response_model=List[schemas.PostVoteResponse])
@router.get('/posts')
def get_posts(db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(oauth2.get_current_user), 
   limit: int = 10, skip:int = 0, search: Optional[str] = ""):

    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    # print(posts)
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    return results



@router.post('/posts')
def post_posts(payload: dict = Body(...)):
    return {'data': 'This is your post API'}


@router.post('/posts2', status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def post_post2(payload2: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(oauth2.get_current_user)): 

    # Method 1  
    # post_dict = payload2.dict()
    # post_dict["id"] = randrange(0,1000000)
    # my_posts.append(post_dict)
    # print(payload2.dict())
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (payload2.title, payload2.content, payload2.published))
    # new_post = cursor.fetchone()
    # conn.commit()


    # Method 2
    # new_post = models.Post(title=payload2.title, content=payload2.content, published=payload2.published)
    # db.add(new_post)
    # db.commit()
    # db.refresh(new_post)
    # return {'msg': new_post}

    # Method 3

    print(current_user.email)
    new_post = models.Post(user_id = current_user.id,**payload2.dict())
    print(new_post)
    db.add(new_post)    
    db.commit()
    db.refresh(new_post)
    return new_post




@router.get("/posts/{id}", response_model=schemas.PostResponse)
def get_post2(id: int, response: Response, db: Session = Depends(get_db)):
    #post = find_post(id)

    #Method 1
    # cursor.execute("""SELECT * from posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()

    # Method 2
    post = db.query(models.Post).filter(models.Post.id == id).first()
     
    if not post:
        #response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return post


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    #index = find_index(id)

    #Method 1
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    #Method 2
    post = db.query(models.Post).filter(models.Post.id == id)

    print(post)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    if post.first().user_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action")

    post.delete(synchronize_session=False)
    db.commit()

    # my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/posts/{id}")
def update_posts(id: int, post:schemas.PostCreate, db: Session = Depends(get_db)):
    #index = find_index(id)


    #Method 1
    # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()


    #Method 2
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post1 = post_query.first()

    if post1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")  

    post_query.update(post.dict(), synchronize_session=False)

    db.commit()

    return {"data": "SUCCESS"}
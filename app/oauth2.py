from . import models
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app import database
from . import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')



SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes




def create_access_token(data: dict):
    data_copy = data.copy() 
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_copy.update({"exp":expire})
    encoded_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



async def verify_access_token(token: str, credentials_exception):
  
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError as e:     
        print(e)  
        raise credentials_exception
   
    return token_data


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#   credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#   detail="Could not validate token", headers={"WWW-Authenticate": "Bearer"})

#   return verify_access_token(token, credentials_exception)


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
  credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
  detail="Could not validate token", headers={"WWW-Authenticate": "Bearer"})

  token = await verify_access_token(token, credentials_exception)
  print(token.id)
  user = db.query(models.User).filter(models.User.id == token.id).first()
 
  return user




 


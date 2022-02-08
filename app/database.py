from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABAE_URL =f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABAE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="ApiDevelopment", user="postgres", password="12345",
#         cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Dataase connection was successfull")
#         break
    
#     except Exception as error:
#         print("can't connect to database")
#         print("Error: ", error)
#         time.sleep(2)
    

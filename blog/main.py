from fastapi import FastAPI
from . import schemas
from .database import engine, Base, SessionLocal

app = FastAPI()

db = SessionLocal()

@app.post('/blog')
def create(request: schemas.Blog, db):
    # db.insert(request)
    # db.commit()
    # db.refresh(request)
    return request


# @app.on_event('startup')
# def create_db():
#     Base.metadata.create_all(bind=engine)

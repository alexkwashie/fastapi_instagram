from os import name
from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from app.db import models
from app.db.database import engine, get_db
from fastapi import Depends
from app.routers import comment, user, post
from fastapi.staticfiles import StaticFiles
from app.auth import authentication
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

@app.get("/")
def root():
  return "Hello world!"


origins = [
  'http://localhost:3000',
  'http://localhost:3001',
  'http://localhost:3002'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


models.Base.metadata.create_all(bind=engine)

app.mount('/images', StaticFiles(directory='app/images'), name='images')

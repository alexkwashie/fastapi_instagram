from sqlalchemy.orm.session import Session
from instagram.routers.schema import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from instagram.db.database import get_db
from instagram.db import db_user

router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)
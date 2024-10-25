from fastapi import APIRouter, Depends, HTTPException
from typing import Optional, List
from db.db_setup import get_db
from sqlalchemy.orm import Session
from schemas.user import UserCreate, User
from api.crud.users import (
    # rename endpoints in case of naming conflict
    get_user,
    get_user_by_email,
    get_users,
    create_user
)

# setting up router (similar to blueprint in flask)
router = APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users



@router.post("/users")
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


# # path params
# # query params
# @router.get("/users/{id}")
# async def get_user(id: int):
#     return { "user": users[id] }
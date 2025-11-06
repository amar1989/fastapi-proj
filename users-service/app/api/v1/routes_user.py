# app/api/v1/routes_user.py
from typing import List
from fastapi import APIRouter, HTTPException, Query, status
from app.schemas.user_schema import UserCreate, UserRead
from app.db.memory import create_user, get_user, list_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_api(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}", response_model=UserRead)
def get_user_api(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[UserRead])
def list_users_api(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    return list_users(offset=offset, limit=limit)

# app/db/memory.py
from typing import Dict, Optional, List
from app.schemas.user_schema import UserCreate, UserRead

# In-memory "database"
_USERS: Dict[int, UserRead] = {}
_NEXT_ID = 1


def create_user(data: UserCreate) -> UserRead:
    """
    Create and store a new user in memory.
    Compatible with Pydantic v1 on Python 3.7 (.dict()).
    """
    global _NEXT_ID
    payload = data.dict()  # if you upgrade to Pydantic v2, use: data.model_dump()
    user = UserRead(id=_NEXT_ID, **payload)
    _USERS[user.id] = user
    _NEXT_ID += 1
    return user


def get_user(user_id: int) -> Optional[UserRead]:
    """
    Fetch a user by ID; returns None if not found.
    """
    return _USERS.get(user_id)


def list_users(offset: int = 0, limit: int = 50) -> List[UserRead]:
    """
    Return a paginated list of users.
    Uses typing.List[...] to work on Python 3.7.
    """
    items = list(_USERS.values())
    return items[offset : offset + limit]

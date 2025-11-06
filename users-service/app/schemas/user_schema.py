from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., gt=0, lt=120)

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
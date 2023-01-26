from typing import Optional
from uuid import UUID

from datetime import date
from pydantic import BaseModel, Field
from pydantic import EmailStr


class UserBase(BaseModel):
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=32)


class User(UserBase):
    id: UUID = Field(...)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birthday: Optional[date] = Field(default=None)

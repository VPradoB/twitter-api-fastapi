from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, EmailStr, BaseModel


class BaseUserDto(BaseModel):
    username: str = Field(..., min_length=4, max_length=20)

class LoginUserDto(BaseUserDto):
    password: str = Field(..., min_length=8, max_length=20)


class ProfileUserDto(BaseUserDto):
    """Profile DTO."""
    email: EmailStr = Field(...)
    birthdate: datetime = Field(...)
    message: Optional[str] = Field(default=None)
    profile_name: str = Field(..., min_length=4, max_length=20)


class UserDto(ProfileUserDto):
    """User DTO."""
    id: UUID = Field(...)
    followers_count: int = Field(...)
    following_count: int = Field(...)
    tweet_count: int = Field(...)
    profile_picture: Optional[str] = Field(default='')
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


class RegisterUserDto(LoginUserDto, ProfileUserDto):
    pass

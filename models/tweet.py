from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from models.user import User


class TweetBase(BaseModel):
    id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)


class TweetCreate(TweetBase):
    user_id: UUID = Field(...)


class TweetInDB(TweetCreate):
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())


class Tweet(TweetInDB):
    user: Optional[User] = Field(default=None)


from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from models.user import User


class Tweet(BaseModel):
    id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    by: User = Field(...)
    created_at: datetime = Field(..., default=datetime.now())
    updated_at: datetime = Field(..., default=datetime.now())

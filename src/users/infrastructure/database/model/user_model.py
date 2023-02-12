from datetime import datetime
from typing import List

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, relationship

from src.shared.config.database import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user'
    id: Mapped[BaseModel.uuid_pk]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    profile_name: Mapped[str]
    profile_description: Mapped[str]
    followers_count: Mapped[int]
    following_count: Mapped[int]
    tweet_count: Mapped[int]
    profile_picture: Mapped[str]
    birthdate: Mapped[datetime]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    followers: Mapped[List["UserModel"]] = relationship(back_populates="UserModel")
    following: Mapped[List["UserModel"]] = relationship(back_populates="UserModel")

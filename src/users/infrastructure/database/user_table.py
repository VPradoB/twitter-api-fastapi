from uuid import UUID, uuid4
from datetime import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.shared.infrastructure.database import Base
from src.users.infrastructure.database.user_followers_table import user_followers_table


class UserInDB(Base):
    __tablename__ = 'user'
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str]
    username: Mapped[str]
    profile_name: Mapped[str]
    hashed_password: Mapped[str]
    profile_description: Mapped[str] = mapped_column(default='')
    followers_count: Mapped[int] = mapped_column(default=0)
    following_count: Mapped[int] = mapped_column(default=0)
    followers: Mapped[List["UserInDB"]] = relationship(secondary=user_followers_table,
                                                       primaryjoin=id == user_followers_table.c.followed_id,
                                                       secondaryjoin=id == user_followers_table.c.follower_id,
                                                       back_populates="followed"
                                                       )
    followed: Mapped[List["UserInDB"]] = relationship(secondary=user_followers_table,
                                                      primaryjoin=id == user_followers_table.c.follower_id,
                                                      secondaryjoin=id == user_followers_table.c.followed_id,
                                                      back_populates="followers"
                                                      )
    tweet_count: Mapped[int] = 0
    profile_picture: Mapped[str]
    birthdate: Mapped[datetime]

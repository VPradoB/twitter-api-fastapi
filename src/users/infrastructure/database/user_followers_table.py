from sqlalchemy import Table, Column, ForeignKey

from src.shared.infrastructure.database import Base

user_followers_table = Table(
    "user_follows_user",
    Base.metadata,
    Column("follower_id", ForeignKey("user.id"), primary_key=True),
    Column("followed_id", ForeignKey("user.id"), primary_key=True),
)

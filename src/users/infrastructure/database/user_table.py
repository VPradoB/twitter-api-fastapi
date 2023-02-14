import uuid

from sqlalchemy import Table, Column, Integer, String, DateTime, UUID, Text
from sqlalchemy.orm import registry

from src.users.domain.user_entity import UserEntity

def create_table(metadata):
    user_table = Table(
        "user",
        metadata,
        Column("id",  Text(length=36), default=lambda: str(uuid.uuid4()),  primary_key=True),
        Column("username", String(15), unique=True),
        Column("email", String(30), unique=True),
        Column("profile_name", String(15)),
        Column("hashed_password", String(32)),
        Column("profile_description", String(250)),
        Column("followers_count", Integer),
        Column("following_count", Integer),
        Column("tweet_count", Integer),
        Column("profile_picture", String(150)),
        Column("birthdate", DateTime),
        Column("created_at", DateTime),
        Column("updated_at", DateTime),
    )

    mapper_registry = registry(metadata=metadata)
    mapper_registry.map_imperatively(UserEntity, user_table)

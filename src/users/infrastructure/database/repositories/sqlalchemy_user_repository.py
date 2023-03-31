from typing import List

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from src.shared.infrastructure.database import Database
from src.shared.infrastructure.sqlalchemy_repository import SQLAlchemyRepository
from src.users.domain.user_entity import IUserRepository, UserEntity
from src.users.infrastructure.database import user_follows_user


class SqlAlchemyUserRepository(IUserRepository, SQLAlchemyRepository):
    """UserEntity repository."""
    db: Session = Database.session

    def get_by_id(self, user_id: str) -> UserEntity | None:
        user = self.db.query(UserEntity).filter_by(id=user_id).first()
        user.tweet_service = None
        user.repository = self
        return user

    def follow(self, follower_id, followed_id):
        pass

    def get_followed(self, user_id):
        pass

    def get_profile_picture(self, user_id):
        pass

    def get_followers(self, user_id):
        pass

    def get_by_email(self, email):
        pass

    def get_all(self) -> List[UserEntity]:
        users = self.db.query(UserEntity).all()
        for user in users:
            user.repository = self
            user.tweet_service = None
        return users

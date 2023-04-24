from typing import List

from sqlalchemy.orm import Session

from src.users.domain.user_entity import IUserRepository, UserEntity
from src.shared.infrastructure.database import Database
from src.users.infrastructure.database.sqlalchemy_user_mapper import UserMapper


class SqlAlchemyUserRepository(IUserRepository):
    """UserEntity repository."""

    def get(self, id):
        pass

    def save(self, user: UserEntity) -> UserEntity:
        with Session(Database.engine) as session:
            user_in_db = UserMapper.to_database(user=user)
            session.add(user_in_db)
            session.commit()
            return user

    def delete(self, id):
        pass

    def get_by_id(self, user_id: str) -> UserEntity | None:
        pass

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
        pass

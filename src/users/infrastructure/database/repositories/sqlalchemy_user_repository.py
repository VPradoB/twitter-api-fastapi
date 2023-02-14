from sqlalchemy.orm import Session

from src.shared.infrastructure.database import Database
from src.shared.infrastructure.sqlalchemy_repository import SQLAlchemyRepository
from src.users.domain.user_entity import IUserRepository, UserEntity


class SqliteUserRepository(IUserRepository, SQLAlchemyRepository):
    """UserEntity repository."""
    db = Database.session

    def get_following(self, user_id):
        pass

    def get_profile_picture(self, user_id):
        pass

    def get_followers(self, user_id):
        pass

    def get_by_email(self, email):
        pass

    def find_by_email(self, email):
        pass

    def find_by_id(self, id):
        pass

    def find_by_username(self, username):
        pass

import abc
from dataclasses import dataclass, field
import uuid
from datetime import datetime
from uuid import UUID

from src.shared.domain.entity import IEntity
from src.shared.domain.repositories import IRepository
from src.shared.domain.services import ITweetService


class IUserRepository(IRepository):
    """Abstract class for user repositories."""

    @abc.abstractmethod
    def get_by_email(self, email):
        pass

    @abc.abstractmethod
    def get_followers(self, user_id):
        pass

    @abc.abstractmethod
    def get_following(self, user_id):
        pass

    @abc.abstractmethod
    def get_profile_picture(self, user_id):
        pass

    @abc.abstractmethod
    def find_by_email(self, email):
        pass

    @abc.abstractmethod
    def find_by_id(self, id):
        pass

    @abc.abstractmethod
    def find_by_username(self, username):
        pass


@dataclass(slots=True)  # using slots to improve performance, but it's not compatible with inheritance
class UserEntity(IEntity):
    """User Entity."""

    email: str
    username: str
    profile_name: str
    hashed_password: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    profile_description: str = field(default='', repr=False)
    followers_count: int = 0
    following_count: int = 0
    tweet_count: int = 0
    profile_picture: str = field(default='', repr=False)
    birthdate: datetime | None = None

    created_at: datetime = field(default_factory=datetime.now, repr=False)
    updated_at: datetime = field(default_factory=datetime.now, repr=False)

    repository: IUserRepository | None = None
    tweet_service: ITweetService | None = None

    def verify_username_availability(self) -> str:
        """Verify if there is no other user with the same username. If there is, raise an exception"""
        return self.username

    def verify_email_availability(self) -> str:
        """Verify if there is no other user with the same email. If there is, raise an exception"""
        return self.email

    @staticmethod
    def hash_password(password) -> str:
        return password

    def get_tweets(self):
        return self.tweet_service.get_by_user_id(self.id)

    def get_followers(self):
        return self.repository.get_followers(self.id)

    def get_following(self):
        return self.repository.get_following(self.id)

    def get_profile_picture(self):
        return self.repository.get_profile_picture(self.profile_picture)

    def save(self):
        return self.repository.save(self)

    def without_password(self):
        return {k: v for k, v in vars(self).items() if k != 'password'}

    @classmethod
    def register(cls, username, email, profile_name, birthdate, password, repository,
                 profile_description='') -> 'UserEntity':
        user = cls(
            username=username,
            email=email,
            profile_name=profile_name,
            birthdate=birthdate,
            hashed_password=cls.hash_password(password),
            profile_description=profile_description,
            repository=repository,
        )
        user.save()
        return user

import abc
from datetime import datetime
from typing import Optional
from uuid import UUID

from src.shared.domain.model import IModel
from src.shared.domain.repositories import IRepository
from src.shared.domain.services import ITweetService


class UserBase(IModel):
    def __init__(self,
                 email: str,
                 username: str,
                 profile_name: str,
                 user_id: UUID,
                 message: Optional[str] = None,
                 followers_count: int = 0,
                 following_count: int = 0,
                 tweet_count: int = 0,
                 profile_picture: Optional[str] = None,
                 birthdate: Optional[datetime] = None,
                 created_at: datetime = datetime.now(),
                 updated_at: datetime = datetime.now(),
                 tweet_service: Optional[ITweetService] = None,
                 repository: Optional['IUserRepository'] = None,
                 ):
        self.id = user_id
        self.username = username
        self.profile_name = profile_name
        self.email = email
        self.birthdate = birthdate
        self.message = message
        self.followers_count = followers_count
        self.following_count = following_count
        self.tweet_count = tweet_count
        self.profile_picture = profile_picture

        self.created_at = created_at
        self.updated_at = updated_at

        self.repository = repository
        self.tweet_service = tweet_service

    def get_tweets(self):
        return self.tweet_service.get_by_user_id(self.id)

    def get_followers(self):
        return self.repository.get_followers(self.id)

    def get_following(self):
        return self.repository.get_following(self.id)

    def get_profile_picture(self):
        return self.repository.get_profile_picture(self.profile_picture)

    def save(self):
        self.repository.save(self)
        return self

    @classmethod
    def hash_password(cls, password) -> str:
        return password


class User(UserBase):
    password: str

    def __init__(self, password: str, **kwargs):
        super().__init__(**kwargs)
        self.password = self.hash_password(password)

    def without_password(self):
        return {k: v for k, v in vars(self).items() if k != 'password'}


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

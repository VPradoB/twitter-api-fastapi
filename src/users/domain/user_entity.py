import abc
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Union

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
    def get_followed(self, user_id):
        pass

    @abc.abstractmethod
    def get_profile_picture(self, user_id):
        pass

    @abc.abstractmethod
    def get_by_id(self, id):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def follow(self, follower_id: str, followed_id: str):
        pass


@dataclass(slots=True)  # using slots to improve performance, but it's not compatible with inheritance
class UserEntity(IEntity):
    """UserInDB Entity."""

    email: str
    username: str
    profile_name: str
    hashed_password: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    profile_description: str = field(default='', repr=False)
    followers_count: int = 0
    following_count: int = 0
    followers: List['UserEntity'] = field(default_factory=list, repr=False)
    followed: List['UserEntity'] = field(default_factory=list, repr=False)
    tweet_count: int = 0
    profile_picture: str = field(default='', repr=False)
    birthdate: datetime | None = None

    created_at: datetime = field(default_factory=datetime.now, repr=False)
    updated_at: datetime = field(default_factory=datetime.now, repr=False)

    repository: IUserRepository | None = None

    def verify_username_availability(self) -> str:
        """Verify if there is no other user with the same username. If there is, raise an exception"""
        return self.username

    def verify_email_availability(self) -> str:
        """Verify if there is no other user with the same email. If there is, raise an exception"""
        return self.email

    def get_followers(self):
        return self.repository.get_followers(self.id)

    def get_following(self):
        return self.repository.get_following(self.id)

    def get_profile_picture(self):
        return self.repository.get_profile_picture(self.profile_picture)

    def save(self):
        return self.repository.save(self)

    def follow(self, user: Union['UserEntity', str]) -> 'UserEntity':
        """Follows a user.
            Args:
                user (UserEntity | str): UserInDB to follow
        """
        if user == self or user.id == self.id:
            raise ValueError('You cannot follow yourself')

        user = user if isinstance(user, UserEntity) else self.repository.get_by_id(user)
        self.followed.append(user)
        return self.repository.follow(self.id, user.id)

    def unfollow(self, user: Union['UserEntity', str]) -> 'UserEntity':
        """Unfollows a user.
            Args:
                user (UserEntity | str): UserInDB to unfollow
        """
        if user == self or user.id == self.id:
            raise ValueError('You cannot unfollow yourself')

        user = user.id if isinstance(user, UserEntity) else user
        self.followed.remove(user)
        return self.repository.save(self)

    def is_following(self, user: Union['UserEntity', str]) -> bool:
        """Checks if the user is following another user.
            Args:
                user (UserEntity | str): UserInDB to check
        """
        user = user.id if isinstance(user, UserEntity) else user
        return user in self.followed

    def is_followed_by(self, user: Union['UserEntity', str]) -> bool:
        """Checks if the user is followed by another user.
            Args:
                user (UserEntity | str): UserInDB to check
        """
        user = user.id if isinstance(user, UserEntity) else user
        return user in self.followers

    def toggle_follow(self, user: Union['UserEntity', str]) -> 'UserEntity':
        """Toggles follow/unfollow a user.
            Args:
                user (UserEntity | str): UserInDB to toggle follow
        """
        if self.is_following(user):
            return self.unfollow(user)
        return self.follow(user)

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
            hashed_password=password,
            profile_description=profile_description,
            repository=repository,
        )
        user.save()
        return user

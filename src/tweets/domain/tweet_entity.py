import abc
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from src.shared.domain.entity import IEntity
from src.shared.domain.repositories import IRepository
from src.shared.domain.services import IUserService


class TweetEntity(IEntity):
    def __init__(
        self,
        user_id,
        content: str,
        likes: int = 0,
        shares: int = 0,
        quotes: int = 0,
        views: int = 0,
        tweet_id: UUID = UUID(),
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
        user_service: Optional[IUserService] = None,
        repository: Optional["ITweetRepository"] = None,
        tweet_quoted_id: Optional["TweetEntity"] = None,
        user=None,
        tweet_quoted: Optional["TweetEntity"] = None,
        tweets_quoted_me: Optional[List["TweetEntity"]] = None,
    ):
        """TweetEntity constructor."""
        self.id = tweet_id
        self.content = content
        self.likes = likes
        self.shares = shares
        self.quotes = quotes
        self.views = views

        self.tweet_quoted_id = tweet_quoted_id
        if user_id is None:
            raise ValueError("UserEntity id is required")
        self.user_id = user_id

        self.user = user
        self.tweet_quoted = tweet_quoted
        self.tweets_quoted_me = tweets_quoted_me

        self.created_at = created_at
        self.updated_at = updated_at

        self.user_service = user_service
        self.repository = repository
        self.tweet_quoted_id = tweet_quoted_id

    def get_user(self):
        return self.user_service.get(self.user_id)

    def save(self):
        self.repository.save(self)

    def get_quoted_tweet(self) -> Optional["TweetEntity"]:
        self.tweet_quoted = self.repository.get(self.tweet_quoted_id)
        return self.tweet_quoted

    def get_tweet_quoted_me(self) -> Optional[List["TweetEntity"]]:
        self.tweets_quoted_me = self.repository.get_by_tweet_quoted_id(self.id)
        return self.tweets_quoted_me


class ITweetRepository(IRepository):
    """Abstract class for tweet repositories."""

    @abc.abstractmethod
    def get_by_tweet_quoted_id(self, tweet_id):
        pass

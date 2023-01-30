import abc
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from src.shared.domain.model import need_attribute, IModel
from src.shared.domain.repositories import IRepository
from src.shared.domain.services import IUserService


class Tweet(IModel):
    def __init__(self,
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
                 repository: Optional['ITweetRepository'] = None,
                 tweet_quoted_id: Optional['Tweet'] = None,
                 user=None,
                 tweet_quoted: Optional['Tweet'] = None,
                 tweets_quoted_me: Optional[List['Tweet']] = None,
                 ):
        """Tweet constructor."""
        self.id = tweet_id
        self.content = content
        self.likes = likes
        self.shares = shares
        self.quotes = quotes
        self.views = views

        self.tweet_quoted_id = tweet_quoted_id
        if user_id is None:
            raise ValueError('User id is required')
        self.user_id = user_id

        self.user = user
        self.tweet_quoted = tweet_quoted
        self.tweets_quoted_me = tweets_quoted_me

        self.created_at = created_at
        self.updated_at = updated_at

        self.user_service = user_service
        self.repository = repository
        self.tweet_quoted_id = tweet_quoted_id

    @need_attribute('user_service')
    def get_user(self):
        return self.user_service.get(self.user_id)

    @need_attribute('repository')
    def save(self):
        self.repository.save(self)

    @need_attribute('repository')
    def get_quoted_tweet(self) -> Optional['Tweet']:
        self.tweet_quoted = self.repository.get(self.tweet_quoted_id)
        return self.tweet_quoted

    @need_attribute('repository')
    def get_tweet_quoted_me(self) -> Optional[List['Tweet']]:
        self.tweets_quoted_me = self.repository.get_by_tweet_quoted_id(self.id)
        return self.tweets_quoted_me


class ITweetRepository(IRepository):
    """Abstract class for tweet repositories."""

    @abc.abstractmethod
    def get_by_tweet_quoted_id(self, tweet_id):
        pass

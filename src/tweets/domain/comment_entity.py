import abc
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from src.shared.domain.entity import IEntity
from src.shared.domain.repositories import IRepository
from src.shared.domain.services import IUserService, ITweetService


class CommentEntity(IEntity):
    def __init__(self,
                 content: str,
                 user_id,
                 tweet_id: UUID,
                 comment_id: UUID = UUID(),
                 reply_to_id: Optional[UUID] = None,
                 user=None,
                 tweet=None,
                 replies_to_me: Optional[List['CommentEntity']] = None,
                 reply_to: Optional['CommentEntity'] = None,
                 repository: Optional['ICommentRepository'] = None,
                 user_service: Optional[IUserService] = None,
                 tweet_service: Optional[ITweetService] = None,
                 created_at: datetime = datetime.now(),
                 updated_at: datetime = datetime.now(),
                 ):
        """CommentEntity constructor."""
        self.id = comment_id
        self.content = content
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.reply_to_id = reply_to_id

        self.user = user
        self.tweet = tweet
        self.reply_to = reply_to
        self.replies_to_me = replies_to_me

        self.created_at = created_at
        self.updated_at = updated_at

        self.repository = repository
        self.user_service = user_service
        self.tweet_service = tweet_service

    def save(self):
        self.repository.save(self)

    def get_user(self):
        self.user = self.user_service.get(self.user_id)
        return self.user

    def get_tweet(self):
        self.tweet = self.tweet_service.get(self.tweet_id)
        return self.tweet

    def get_reply_to(self):
        self.reply_to = self.repository.get(self.reply_to_id)
        return self.reply_to

    def get_reply_to_me(self):
        self.replies_to_me = self.repository.get_by_reply_to(self.id)
        return self.replies_to_me


class ICommentRepository(IRepository):
    """Abstract class for comment repositories."""

    @abc.abstractmethod
    def get_by_user_id(self, user_id) -> Optional[List[CommentEntity]]:
        pass

    @abc.abstractmethod
    def get_by_reply_to(self, comment_id) -> Optional[List[CommentEntity]]:
        pass

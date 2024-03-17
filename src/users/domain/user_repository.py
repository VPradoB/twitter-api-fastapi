import abc

from src.shared.domain.Criteria.criteria import Criteria


class UserRepository(abc.ABC):
    """Abstract class for user repositories."""

    @abc.abstractmethod
    def matching(self, criteria: Criteria) -> list["UserEntity"]:
        """Returns a list of users that match the criteria."""

    @abc.abstractmethod
    def get_profile_picture(self, user_id):
        pass

    @abc.abstractmethod
    def follow(self, follower_id: str, followed_id: str) -> None:
        """Follows a user."""

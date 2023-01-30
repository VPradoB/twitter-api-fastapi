import abc


class IUserService(abc.ABC):
    """Abstract class for user services."""

    @abc.abstractmethod
    def get(self, user_id):
        pass

    @abc.abstractmethod
    def save(self, entity):
        pass

class ITweetService(abc.ABC):
    """Abstract class for tweet services."""

    @abc.abstractmethod
    def get(self, tweet_id):
        pass

    @abc.abstractmethod
    def save(self, entity):
        pass

    def get_by_user_id(self, user_id):
        pass

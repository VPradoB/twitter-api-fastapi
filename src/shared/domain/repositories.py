import abc


class IRepository(abc.ABC):
    """Abstract class for repositories."""

    @abc.abstractmethod
    def get(self, id):
        pass

    @abc.abstractmethod
    def save(self, entity):
        pass

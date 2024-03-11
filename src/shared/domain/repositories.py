import abc


class IRepository(abc.ABC):
    """Abstract class for repositories."""

    @abc.abstractmethod
    def get(self, id):
        pass

    @abc.abstractmethod
    def save(self, entity):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def get_all(self, ids):
        pass

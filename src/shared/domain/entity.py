import abc


class IEntity(abc.ABC):
    """Abstract class for tables."""

    @abc.abstractmethod
    def save(self):
        pass

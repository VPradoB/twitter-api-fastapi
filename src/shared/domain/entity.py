import abc

class IEntity(abc.ABC):
    """Abstract class for models."""

    @abc.abstractmethod
    def save(self):
        pass
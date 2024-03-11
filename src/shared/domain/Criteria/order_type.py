from dataclasses import dataclass
from enum import Enum


class OrderTypes(Enum):
    ASC = "asc"
    DESC = "desc"
    NONE = "none"


@dataclass(frozen=True)
class OrderType:
    _value: OrderTypes

    @property
    def value(self) -> str:
        return self._value.value

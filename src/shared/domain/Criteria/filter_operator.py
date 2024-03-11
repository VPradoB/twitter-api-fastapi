from dataclasses import dataclass
from enum import Enum


class OperatorsTypes(Enum):
    EQUAL = "="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    START_WITH = "start_with"
    END_WITH = "end_with"


@dataclass(frozen=True)
class FilterOperator:
    _value: OperatorsTypes

    @property
    def value(self) -> str:
        return self._value.value

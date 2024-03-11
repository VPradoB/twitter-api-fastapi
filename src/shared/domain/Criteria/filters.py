from typing import TypedDict

from src.shared.domain.Criteria.filter import Filter


class FiltersPrimitives(TypedDict):
    field: str
    operator: str
    value: str


class Filters:
    def __init__(self, filters: list[Filter]):
        self.filters = filters

    @classmethod
    def from_primitives(cls, filters: list[FiltersPrimitives]) -> "Filters":
        return cls(
            filters=[
                Filter.from_primitives(
                    f.get("field"), f.get("operator"), f.get("value")
                )
                for f in filters
            ]
        )

from typing import TypedDict

from src.shared.domain.Criteria.filters import Filters, FiltersPrimitives
from src.shared.domain.Criteria.order import Order


class CriteriaPrimitives(TypedDict):
    filters: list[FiltersPrimitives]
    order_by: str
    order_type: str


class Criteria:
    def __init__(self, filters: Filters, order: Order):
        self.filters = filters
        self.order = order

    @classmethod
    def from_primitives(
        cls,
        criteria_primitives: CriteriaPrimitives,
    ) -> "Criteria":
        return Criteria(
            filters=Filters.from_primitives(criteria_primitives.get("filters")),
            order=Order.from_primitives(criteria_primitives.get("order_by"), criteria_primitives.get("order_type")),
        )

    def to_primitives(self) -> "CriteriaPrimitives":
        return {
            "filters": self.filters.to_primitives(),
            "order_by": self.order.order_by.value,
            "order_type": self.order.order_type.value,
        }

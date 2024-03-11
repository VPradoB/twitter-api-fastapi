from src.shared.domain.Criteria.filters import Filters, FiltersPrimitives
from src.shared.domain.Criteria.order import Order


class Criteria:
    def __init__(self, filters: Filters, order: Order):
        self.filters = filters
        self.order = order

    @classmethod
    def from_primitives(
        cls,
        filters: list[FiltersPrimitives],
        order_by: str | None,
        order_type: str | None,
    ) -> "Criteria":
        return Criteria(
            filters=Filters.from_primitives(filters),
            order=Order.from_primitives(order_by, order_type),
        )

from src.shared.domain.Criteria.order_by import OrderBy
from src.shared.domain.Criteria.order_type import OrderType, OrderTypes


class Order:
    def __init__(self, order_by: OrderBy, order_type: OrderType):
        self.order_by = order_by
        self.order_type = order_type

    @classmethod
    def none(cls) -> "Order":
        return cls(OrderBy(""), OrderType(OrderTypes.NONE))

    @classmethod
    def from_primitives(cls, order_by: str, order_type: str) -> "Order":
        return cls(OrderBy(order_by), OrderType(OrderTypes(order_type)))

    def to_primitives(self) -> dict:
        return {
            "order_by": self.order_by.value,
            "order_type": self.order_type.value,
        }

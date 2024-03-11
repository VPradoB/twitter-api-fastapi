from src.shared.domain.Criteria.filter_field import FilterField
from src.shared.domain.Criteria.filter_operator import FilterOperator, OperatorsTypes
from src.shared.domain.Criteria.filter_value import FilterValue


class Filter:
    def __init__(
        self, field: FilterField, operator: FilterOperator, value: FilterValue
    ):
        self.field = field
        self.operator = operator
        self.value = value

    @classmethod
    def from_primitives(cls, field: str, operator: str, value: str) -> "Filter":
        return cls(
            FilterField(field),
            FilterOperator(OperatorsTypes(operator)),
            FilterValue(value),
        )

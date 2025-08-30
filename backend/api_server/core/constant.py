from enum import Enum


class AuditState(Enum):
    """
    Enum for audit entry states.
    ref: https://docs.python.org/3/howto/enum.html#when-to-use-new-vs-init
    """

    ENTITY_ADDED = (0, "entityAdded")
    ENTITY_MODIFIED = (1, "entityModified")
    ENTITY_DELETED = (2, "entityDeleted")

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj

    @classmethod
    def get_by_value(cls, value: int):
        """Get enum member by its integer value."""
        for state in cls:
            if state.value == value:
                return state
        raise ValueError(f"No AuditState with value {value}")

    @classmethod
    def get_by_name(cls, name: str):
        """Get enum member by its state name."""
        for state in cls:
            if state.state_name == name:
                return state
        raise ValueError(f"No AuditState with name {name}")

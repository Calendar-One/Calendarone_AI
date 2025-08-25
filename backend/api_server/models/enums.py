from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class EnumType(BaseModel):
    """
    Enum Type model for defining different types of enums.
    """

    __tablename__ = "enum_types"

    enum_type_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relationships
    enum_values = relationship("EnumValue", back_populates="enum_type")


class EnumValue(BaseModel):
    """
    Enum Value model for storing specific enum values.
    """

    __tablename__ = "enum_values"

    enum_value_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    enum_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_types.enum_type_id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    order: Mapped[int] = mapped_column(Integer, nullable=True)

    # Relationships
    enum_type = relationship("EnumType", back_populates="enum_values")

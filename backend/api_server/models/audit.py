from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api_server.models.base import Base


class AuditEntry(Base):
    """
    Model for audit entries that track changes to entities.
    """

    __tablename__ = "audit_entry"

    audit_entry_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    created_by: Mapped[str] = mapped_column(String(100), nullable=True)
    created_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    entity_set_name: Mapped[str] = mapped_column(String(255), nullable=False)
    entity_type_name: Mapped[str] = mapped_column(String(255), nullable=False)

    state: Mapped[int] = mapped_column(Integer, nullable=False)
    state_name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relationship to audit entry properties
    properties: Mapped[list["AuditEntryProperty"]] = relationship(
        "AuditEntryProperty", back_populates="audit_entry", cascade="all, delete-orphan"
    )


class AuditEntryProperty(Base):
    """
    Model for audit entry properties that track specific field changes.
    """

    __tablename__ = "audit_entry_property"

    audit_entry_property_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    audit_entry_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("audit_entry.audit_entry_id"), nullable=False
    )

    property_name: Mapped[str] = mapped_column(String(255), nullable=False)
    new_value: Mapped[str] = mapped_column(Text, nullable=True)
    old_value: Mapped[str] = mapped_column(Text, nullable=True)

    # Relationships
    audit_entry = relationship("AuditEntry", back_populates="properties")

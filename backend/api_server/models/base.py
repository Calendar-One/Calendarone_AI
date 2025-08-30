from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class BaseModel(Base):
    """
    Base model class that provides common fields and functionality
    for all database models.
    """

    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc), nullable=False
    )
    created_by: Mapped[str] = mapped_column(String(100), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        nullable=False,
    )
    updated_by: Mapped[str] = mapped_column(String(100), nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    deleted_by: Mapped[str] = mapped_column(String(100), nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    version: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    def soft_delete(self):
        """Mark the record as deleted without actually removing it from the database."""
        self.is_deleted = True
        self.updated_at = datetime.now(timezone.utc)

    def restore(self):
        """Restore a soft-deleted record."""
        self.is_deleted = False
        self.updated_at = datetime.now(timezone.utc)

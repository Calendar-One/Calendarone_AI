from datetime import datetime
from sqlalchemy import Boolean, DateTime
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
        DateTime, default=datetime.datetime.now(datetime.UTC), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
        nullable=False,
    )
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    def soft_delete(self):
        """Mark the record as deleted without actually removing it from the database."""
        self.is_deleted = True
        self.updated_at = datetime.datetime.now(datetime.UTC)

    def restore(self):
        """Restore a soft-deleted record."""
        self.is_deleted = False
        self.updated_at = datetime.datetime.now(datetime.UTC)

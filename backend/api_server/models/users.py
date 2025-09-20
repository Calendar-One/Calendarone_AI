from datetime import datetime
from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel


class User(BaseModel):
    """
    User model representing application users.
    """

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    refresh_token: Mapped[str] = mapped_column(String, nullable=True)
    refresh_token_expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

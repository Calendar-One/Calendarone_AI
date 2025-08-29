from sqlalchemy import Integer, String
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
    password: Mapped[str] = mapped_column(String(255), nullable=False)

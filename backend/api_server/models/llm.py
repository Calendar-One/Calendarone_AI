from sqlalchemy import String, Integer, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel


class LLModel(BaseModel):
    """
    Large Language Model configuration model.
    """

    __tablename__ = "ll_models"

    llm_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    llm_name: Mapped[str] = mapped_column(String(255), nullable=False)
    context_window: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    cost_per_mill_input_token: Mapped[float] = mapped_column(
        Numeric(10, 6), nullable=True
    )
    cost_per_mill_output_token: Mapped[float] = mapped_column(
        Numeric(10, 6), nullable=True
    )

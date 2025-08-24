from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class Setting(BaseModel):
    """
    Settings model for application configuration.
    """

    __tablename__ = "settings"

    llm_id: Mapped[str] = mapped_column(
        String(255), ForeignKey("ll_models.llm_id"), primary_key=True
    )
    token_limit_monthly: Mapped[int] = mapped_column(Integer, nullable=True)
    token_used: Mapped[int] = mapped_column(Integer, nullable=True)
    token: Mapped[str] = mapped_column(String(255), nullable=True)

    # Relationships
    llm_model = relationship("LLModel", foreign_keys=[llm_id])


class McpServer(BaseModel):
    """
    MCP (Model Context Protocol) Server configuration model.
    """

    __tablename__ = "mcp_servers"

    mcp_server_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    server_name: Mapped[str] = mapped_column(
        String(255), nullable=False
    )  # Fixed typo from "SeverName"
    config: Mapped[str] = mapped_column(String(1000), nullable=True)
    is_enable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

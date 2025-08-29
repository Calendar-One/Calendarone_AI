from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class Setting(BaseModel):
    """
    Settings model for application configuration.
    """

    __tablename__ = "settings"

    setting_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    setting_key: Mapped[str] = mapped_column(String(100), nullable=False)
    setting_value: Mapped[str] = mapped_column(String(1000), nullable=True)


class McpServer(BaseModel):
    """
    MCP (Model Context Protocol) Server configuration model.
    """

    __tablename__ = "mcp_servers"

    mcp_server_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    server_name: Mapped[str] = mapped_column(
        String(255), nullable=False
    )  # Fixed typo from "SeverName"
    description: Mapped[str] = mapped_column(String(), nullable=True)
    config: Mapped[str] = mapped_column(String(1000), nullable=True)
    is_enable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class CloudFile(BaseModel):
    """
    File model for storing file uploads to cloud storage (S3, GCP, etc.).
    """

    __tablename__ = "cloud_files"

    cloud_file_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    original_file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    stored_file_name: Mapped[str] = mapped_column(String(255), nullable=True)
    file_path: Mapped[str] = mapped_column(String(500), nullable=True)
    file_size: Mapped[int] = mapped_column(Integer, nullable=True)
    content_type: Mapped[str] = mapped_column(String(50), nullable=True)

    storage_provider_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )  # 'S3', 'GCP', 'Azure', etc.
    bucket_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_url: Mapped[str] = mapped_column(String(1000), nullable=True)
    upload_status_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )  # 'pending', 'uploaded', 'failed'
    checksum: Mapped[str] = mapped_column(
        String(255), nullable=True
    )  # For file integrity verification

    # Relationships
    upload_status_enum = relationship("EnumValue", foreign_keys=[upload_status_id])
    storage_provider_enum = relationship(
        "EnumValue", foreign_keys=[storage_provider_id]
    )

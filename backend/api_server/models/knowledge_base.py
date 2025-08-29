from sqlalchemy import String, Integer, Boolean, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class KnowledgeBase(BaseModel):
    """
    Knowledge Base configuration model.
    """

    __tablename__ = "knowledge_bases"

    knowledge_base_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    knowledge_base_name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    knowledge_base_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )
    overlap_length: Mapped[int] = mapped_column(Integer, nullable=True)
    length_of_chunk: Mapped[int] = mapped_column(Integer, nullable=True)
    is_load_from_database: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    tags: Mapped[str] = mapped_column(String(500), nullable=True)
    embedding_llm_name_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ll_models.llm_id"), nullable=True
    )

    ranker_llm_name_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ll_models.llm_id"), nullable=True
    )

    # Relationships
    knowledge_base_type = relationship(
        "EnumValue", foreign_keys=[knowledge_base_type_id]
    )
    embedding_llm = relationship("LLModel", foreign_keys=[embedding_llm_name_id])
    ranker_llm = relationship("LLModel", foreign_keys=[ranker_llm_name_id])
    files = relationship("KnowledgeBaseFile", back_populates="knowledge_base")
    urls = relationship("KnowledgeBaseUrl", back_populates="knowledge_base")
    texts = relationship("KnowledgeBaseText", back_populates="knowledge_base")


class KnowledgeBaseFile(BaseModel):
    """
    Knowledge Base File model for storing file-based sources.
    """

    __tablename__ = "knowledge_base_files"

    knowledge_base_file_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    knowledge_base_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("knowledge_bases.knowledge_base_id"), nullable=False
    )

    cloud_file_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("cloud_files.cloud_file_id"), nullable=True
    )
    processing_status: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )
    embedding_ids: Mapped[str] = mapped_column(String(), nullable=True)
    extracted_text: Mapped[str] = mapped_column(Text, nullable=True)
    extraction_metadata: Mapped[dict] = mapped_column(JSON, nullable=True)

    # Relationships
    knowledge_base = relationship("KnowledgeBase", back_populates="files")
    processing_status_enum = relationship("EnumValue", foreign_keys=[processing_status])


class KnowledgeBaseUrl(BaseModel):
    """
    Knowledge Base URL model for storing web-based sources.
    """

    __tablename__ = "knowledge_base_urls"

    knowledge_base_file_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    knowledge_base_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("knowledge_bases.knowledge_base_id"), nullable=False
    )
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    domain_name: Mapped[str] = mapped_column(String(255), nullable=True)
    page_title: Mapped[str] = mapped_column(String(500), nullable=True)
    last_crawled_at: Mapped[str] = mapped_column(DateTime, nullable=True)
    crawl_frequency: Mapped[str] = mapped_column(
        String(100), nullable=True
    )  # interval type
    extracted_text: Mapped[str] = mapped_column(Text, nullable=True)
    extraction_metadata: Mapped[dict] = mapped_column(JSON, nullable=True)
    response_code: Mapped[int] = mapped_column(Integer, nullable=True)
    response_header: Mapped[dict] = mapped_column(JSON, nullable=True)
    content_length: Mapped[int] = mapped_column(Integer, nullable=True)
    content_type: Mapped[str] = mapped_column(String(255), nullable=True)
    processing_status: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )
    embedding_ids: Mapped[str] = mapped_column(String(), nullable=True)
    outbound_links: Mapped[str] = mapped_column(
        Text, nullable=True
    )  # Text[] equivalent
    inbound_link_count: Mapped[int] = mapped_column(Integer, nullable=True)

    # Relationships
    knowledge_base = relationship("KnowledgeBase", back_populates="urls")
    processing_status_enum = relationship("EnumValue", foreign_keys=[processing_status])


class KnowledgeBaseText(BaseModel):
    """
    Knowledge Base Text model for storing text-based sources.
    """

    __tablename__ = "knowledge_base_texts"

    knowledge_base_file_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    knowledge_base_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("knowledge_bases.knowledge_base_id"), nullable=False
    )
    header: Mapped[str] = mapped_column(String(500), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    content_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )
    embedding_processing_status: Mapped[int] = mapped_column(
        Integer, ForeignKey("enum_values.enum_value_id"), nullable=True
    )
    embedding_ids: Mapped[str] = mapped_column(String(), nullable=True)
    outbound_links: Mapped[str] = mapped_column(
        Text, nullable=True
    )  # Text[] equivalent
    inbound_link_count: Mapped[int] = mapped_column(Integer, nullable=True)

    # Relationships
    knowledge_base = relationship("KnowledgeBase", back_populates="texts")
    content_type_enum = relationship("EnumValue", foreign_keys=[content_type_id])
    embedding_processing_status_enum = relationship(
        "EnumValue", foreign_keys=[embedding_processing_status]
    )

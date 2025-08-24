from sqlalchemy import String, Integer, Boolean, Text, ForeignKey
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
    file_ids: Mapped[int] = mapped_column(Integer, nullable=True)
    overlap_length: Mapped[int] = mapped_column(Integer, nullable=True)
    length_of_chunk: Mapped[int] = mapped_column(Integer, nullable=True)
    is_load_from_database: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    embedding_llm_name_id: Mapped[str] = mapped_column(
        String(255), ForeignKey("ll_models.llm_id"), nullable=True
    )
    ranker_llm_name_id: Mapped[str] = mapped_column(
        String(255), ForeignKey("ll_models.llm_id"), nullable=True
    )

    # Relationships
    embedding_llm = relationship("LLModel", foreign_keys=[embedding_llm_name_id])
    ranker_llm = relationship("LLModel", foreign_keys=[ranker_llm_name_id])
    kb_sources = relationship("KnowledgeBaseSource", back_populates="knowledge_base")


class KnowledgeBaseSource(BaseModel):
    """
    Knowledge Base Source model for storing source documents.
    """

    __tablename__ = "knowledge_base_sources"

    knowledge_base_source_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    knowledge_base_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("knowledge_bases.knowledge_base_id"), nullable=False
    )
    file_id: Mapped[int] = mapped_column(Integer, nullable=True)
    header: Mapped[str] = mapped_column(Text, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    craw_web_url: Mapped[str] = mapped_column(String(500), nullable=True)
    file_path: Mapped[str] = mapped_column(String(500), nullable=True)
    process_status: Mapped[str] = mapped_column(String(100), nullable=True)

    # Relationships
    knowledge_base = relationship("KnowledgeBase", back_populates="kb_sources")

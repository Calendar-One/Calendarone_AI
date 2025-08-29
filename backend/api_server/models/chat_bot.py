from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class ChatBot(BaseModel):
    """
    ChatBot configuration model.
    """

    __tablename__ = "chat_bots"

    chat_bot_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    avatar_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("cloud_files.cloud_file_id"), nullable=True
    )

    chat_bot_name: Mapped[str] = mapped_column(String(255), nullable=False)
    prompt_template: Mapped[str] = mapped_column(Text, nullable=True)
    greeting_message: Mapped[str] = mapped_column(Text, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    llm_name_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ll_models.llm_id"), nullable=True
    )

    temperature: Mapped[str] = mapped_column(String(50), nullable=True)
    context_length: Mapped[int] = mapped_column(Integer, nullable=True)
    conversation_rounds: Mapped[int] = mapped_column(Integer, nullable=True)
    knowledge_base_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("knowledge_bases.knowledge_base_id"), nullable=True
    )
    mcp_server_ids: Mapped[str] = mapped_column(
        String(500), nullable=True
    )  # string of mcp server ids separated by comma

    # Relationships
    llm_model = relationship("LLModel", foreign_keys=[llm_name_id])
    knowledge_base = relationship("KnowledgeBase", foreign_keys=[knowledge_base_id])
    conversations = relationship("Conversation", back_populates="chat_bot")
    prompts = relationship("Prompt", back_populates="chat_bot")


class Prompt(BaseModel):
    """
    Prompt template model for chatbots.
    """

    __tablename__ = "prompts"

    prompt_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    prompt_template: Mapped[str] = mapped_column(Text, nullable=False)
    place_holder: Mapped[str] = mapped_column(String(255), nullable=True)
    chat_bot_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("chat_bots.chat_bot_id"), nullable=False
    )

    # Relationships
    chat_bot = relationship("ChatBot", back_populates="prompts")

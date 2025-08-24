from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseModel


class Conversation(BaseModel):
    """
    Conversation model representing chat sessions.
    """

    __tablename__ = "conversations"

    conversation_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    person_profile_id: Mapped[int] = mapped_column(Integer, nullable=True)
    conversation_title: Mapped[str] = mapped_column(
        String(255), nullable=True
    )  # Fixed typo from "ConversionTitle"
    conversation_summary: Mapped[str] = mapped_column(
        Text, nullable=True
    )  # Fixed typo from "ConversionSummary"
    chat_bot_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("chat_bots.chat_bot_id"), nullable=True
    )

    # Relationships
    chat_bot = relationship("ChatBot", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")


class Message(BaseModel):
    """
    Message model representing individual messages in conversations.
    """

    __tablename__ = "messages"

    message_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    person_profile_id: Mapped[int] = mapped_column(Integer, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    content_type_id: Mapped[int] = mapped_column(Integer, nullable=True)
    conversation_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("conversations.conversation_id"), nullable=False
    )
    user_feedback: Mapped[str] = mapped_column(String(500), nullable=True)
    token_used: Mapped[int] = mapped_column(Integer, nullable=True)

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")
    references = relationship("MessageReference", back_populates="message")


class MessageReference(BaseModel):
    """
    MessageReference model for storing document references in messages.
    """

    __tablename__ = "message_references"

    message_reference_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    message_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("messages.message_id"), nullable=False
    )
    doc_url: Mapped[str] = mapped_column(String(500), nullable=True)
    page_num: Mapped[int] = mapped_column(Integer, nullable=True)
    file_name: Mapped[str] = mapped_column(String(255), nullable=True)

    # Relationships
    message = relationship("Message", back_populates="references")

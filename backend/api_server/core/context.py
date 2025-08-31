"""
Application context variables for request-scoped data.
This file centralizes all context variables used across the application.
"""
from contextvars import ContextVar
from typing import Optional

# User context for current authenticated user
current_user_context: ContextVar[Optional[int]] = ContextVar(
    "current_user_id", default=None
)
current_user_name_context: ContextVar[Optional[str]] = ContextVar(
    "current_user_name", default=None
)


def get_current_user_name() -> Optional[str]:
    """Get current user name from context"""
    return current_user_name_context.get()


def set_current_user_name(user_name: str) -> None:
    """Set current user name in context"""
    current_user_name_context.set(user_name)


def get_current_user_id() -> Optional[int]:
    """Get current user ID from context"""
    return current_user_context.get()


def set_current_user_id(user_id: int) -> None:
    """Set current user ID in context"""
    current_user_context.set(user_id)


def clear_user_context() -> None:
    """Clear user context (useful for testing)"""
    current_user_context.set(None)
    current_user_name_context.set(None)

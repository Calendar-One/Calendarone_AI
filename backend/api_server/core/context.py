"""
Application context variables for request-scoped data.
This file centralizes all context variables used across the application.
"""
from contextvars import ContextVar
from typing import Optional
from datetime import datetime

# User context for current authenticated user
current_user_context: ContextVar[Optional[int]] = ContextVar(
    "current_user_id", default=None
)

# Optional: Additional context variables
request_id_context: ContextVar[Optional[str]] = ContextVar("request_id", default=None)
request_start_time_context: ContextVar[Optional[datetime]] = ContextVar(
    "request_start_time", default=None
)


def get_current_user_id() -> Optional[int]:
    """Get current user ID from context"""
    return current_user_context.get()


def set_current_user_id(user_id: int) -> None:
    """Set current user ID in context"""
    current_user_context.set(user_id)


def clear_user_context() -> None:
    """Clear user context (useful for testing)"""
    current_user_context.set(None)

from datetime import timedelta, datetime, timezone
from typing import Optional
from api_server.models.users import User
from sqlalchemy.orm import Session
from jose import jwt
from fastapi import HTTPException
from api_server.core.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str) -> int:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return int(user_id)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_user_by_email(email: str, session: Session) -> User:
    """
    Get a user by email.
    """
    return session.query(User).filter(User.email == email).first()

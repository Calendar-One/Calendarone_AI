import secrets
from datetime import datetime, timedelta, timezone
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from api_server.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    subject: Union[str, Any], name: str | None = None, expires_delta: timedelta = None
) -> str:
    """
    Creates an access token.

    Parameters:
        subject (Union[str, Any]): The subject for which the access token is created.
        expires_delta (timedelta, optional): The expiration time for the access token. Defaults to None.

    Returns:
        str: The encoded access token.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject), "name": name}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Decodes an access token.
    """
    return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify if a plain password matches a hashed password.

    Parameters:
        plain_password (str): The plain password to be verified.
        hashed_password (str): The hashed password to compare with.

    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Generate the hash value of a password.

    Parameters:
        password (str): The password to be hashed.

    Returns:
        str: The hash value of the password.
    """
    return pwd_context.hash(password)


def create_refresh_token() -> str:
    """
    Creates a refresh token using cryptographically secure random bytes.

    Returns:
        str: The refresh token.
    """
    return secrets.token_urlsafe(32)


def verify_refresh_token(token: str, user_refresh_token: str) -> bool:
    """
    Verify if a refresh token matches the user's stored refresh token.

    Parameters:
        token (str): The refresh token to verify.
        user_refresh_token (str): The user's stored refresh token.

    Returns:
        bool: True if the refresh token matches, False otherwise.
    """
    return token == user_refresh_token


def is_refresh_token_expired(expires_at: datetime) -> bool:
    """
    Check if a refresh token has expired.

    Parameters:
        expires_at (datetime): The expiration datetime of the refresh token.

    Returns:
        bool: True if the token is expired, False otherwise.
    """
    if expires_at is None:
        return True
    return datetime.now(timezone.utc) > expires_at


def get_refresh_token_expiration() -> datetime:
    """
    Get the expiration datetime for a new refresh token.

    Returns:
        datetime: The expiration datetime for the refresh token.
    """
    return datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

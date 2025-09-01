from typing import Annotated, Tuple
from api_server.core.config import settings
from api_server.core.log import get_logger
from api_server.database import get_db
from api_server.models.users import User
from api_server.schemas.auth import TokenPayload
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from fastapi import Depends, Query, status
from pydantic import ValidationError
from sqlalchemy.orm import Session


logger = get_logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/{settings.API_VERSION}/auth/login")

LoginForm = Annotated[OAuth2PasswordRequestForm, Depends()]


def get_pagination_params(
    skip: int = Query(0, ge=0), limit: int = Query(10, gt=0)
) -> Tuple[int, int]:
    """
    Get the pagination parameters.

    Parameters:
        skip (int): The number of items to skip. Defaults to 0.
        limit (int): The maximum number of items to return. Defaults to 10.

    Returns:
        Tuple[int, int]: A tuple containing the skip and limit values.
    """
    return skip, limit


def get_token(token: str = Depends(oauth2_scheme)) -> TokenPayload:
    """
    Retrieve the token payload from the provided JWT token.

    Parameters:
        token (str, optional): The JWT token. Defaults to the value returned by the `oauth2_scheme` dependency.

    Returns:
        TokenPayload: The decoded token payload.

    Raises:
        HTTPException: If there is an error decoding the token or validating the payload.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_data


def get_sign_in_db_session(token_data: TokenPayload = Depends(get_token)) -> Session:
    """
    Get the database session for sign in.
    """
    db = next(get_db())
    db.info["user_name"] = token_data.name
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token_data: TokenPayload = Depends(get_token),
    db: Session = Depends(get_sign_in_db_session),
) -> User:
    user = db.query(User).filter(User.user_id == token_data.sub).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
# public session for public routes
SessionDep = Annotated[Session, Depends(get_db)]

# session for private routes
SignInDBSessionDep = Annotated[Session, Depends(get_sign_in_db_session)]

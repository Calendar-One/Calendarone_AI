# Contents of JWT token
from datetime import datetime
from typing import Optional
from api_server.schemas.users import UserResponse
from pydantic import BaseModel


class TokenPayload(BaseModel):
    sub: str | None = None
    name: str | None = None
    exp: Optional[datetime] = None


class RefreshTokenRequest(BaseModel):
    refresh_token: str


# JSON payload containing access token
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse

# Contents of JWT token
from pydantic import BaseModel


class TokenPayload(BaseModel):
    sub: str | None = None
    name: str | None = None


# JSON payload containing access token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

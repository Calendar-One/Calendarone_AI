from api_server.api.dependencies import LoginForm, SessionDep
from api_server.core import security
from api_server.schemas.auth import Token
from api_server.services import user_service
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
async def login(request: LoginForm, db: SessionDep):
    user = user_service.authenticate_user(
        db, email=request.username, password=request.password
    )
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token = security.create_access_token(
        subject=user.user_id, name=user.user_name
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

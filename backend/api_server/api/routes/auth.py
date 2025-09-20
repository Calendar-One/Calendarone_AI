from api_server.api.dependencies import CurrentUser, LoginForm, SessionDep
from api_server.core import security
from api_server.schemas.auth import Token, RefreshTokenRequest
from api_server.schemas.base import ApiResponse
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

    refresh_token = user_service.generate_and_save_refresh_token(db, user)

    user.refresh_token = refresh_token

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.post("/refresh", response_model=Token)
async def refresh_token(request: RefreshTokenRequest, db: SessionDep):
    user = user_service.authenticate_with_refresh_token(db, request.refresh_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = security.create_access_token(
        subject=user.user_id, name=user.user_name
    )

    new_refresh_token = user_service.generate_and_save_refresh_token(db, user)
    user.refresh_token = new_refresh_token

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.post("/logout", response_model=ApiResponse)
async def logout(current_user: CurrentUser, db: SessionDep):
    user_service.revoke_refresh_token(db, current_user)
    return {"message": "Successfully logged out"}

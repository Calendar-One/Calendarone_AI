from api_server.api.dependencies import CurrentUser, SignInDBSessionDep
from api_server.schemas.users import UserBase, UserResponse
from api_server.schemas.base import ApiResponse
from api_server.services import user_service
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/list", response_model=ApiResponse[UserResponse])
def get_users(
    current_user: CurrentUser,
    session: SignInDBSessionDep,
) -> ApiResponse[UserResponse]:
    """
    Make sure the get current user execute before session created,
    because get current user need to set current user name in context,
    and session created need to get current user name from context.

    Get a specific user by id.
    """
    user = user_service.create(
        session,
        UserBase(
            user_name=current_user.user_name + "_test",
            email="test@tesdd1tddd.com",
            hashed_password="test",
            is_active=True,
            is_superuser=False,
        ),
    )
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges",
        )
    return ApiResponse.success(data=user)

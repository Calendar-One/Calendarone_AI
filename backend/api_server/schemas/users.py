from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class UserBase(BaseModel):
    user_name: str = Field(..., description="User's name")
    email: EmailStr = Field(..., description="User's email address")
    hashed_password: str = Field(..., description="User's password")
    is_active: bool = Field(..., description="User's active status")
    is_superuser: bool = Field(..., description="User's superuser status")


class UserLoginRequest(BaseModel):
    """
    DTO for user login request.
    """

    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=1, description="User's password")


class UserLoginResponse(BaseModel):
    """
    DTO for user login response.
    """

    user_id: int = Field(..., description="User's unique identifier")
    user_name: str = Field(..., description="User's display name")
    email: EmailStr = Field(..., description="User's email address")
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")


class UserResetPasswordRequest(BaseModel):
    """
    DTO for password reset request.
    """

    email: EmailStr = Field(..., description="User's email address")


class UserResetPasswordConfirm(BaseModel):
    """
    DTO for password reset confirmation.
    """

    token: str = Field(..., description="Password reset token")
    new_password: str = Field(..., min_length=8, description="New password")
    confirm_password: str = Field(..., description="Password confirmation")

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, v, info):
        if "new_password" in info.data and v != info.data["new_password"]:
            raise ValueError("Passwords do not match")
        return v

    @field_validator("new_password")
    @classmethod
    def validate_password_strength(cls, v):
        """
        Validate password strength requirements.
        """
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        # Check for at least one uppercase letter
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")

        # Check for at least one lowercase letter
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")

        # Check for at least one digit
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")

        return v


class UserResetPasswordResponse(BaseModel):
    """
    DTO for password reset response.
    """

    message: str = Field(..., description="Success message")
    email: EmailStr = Field(..., description="Email address where reset link was sent")


class UserCreateRequest(UserBase):
    """
    DTO for user registration request.
    """

    password: str = Field(..., min_length=8, description="User's password")
    confirm_password: str = Field(..., description="Password confirmation")

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, v, info):
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v):
        """
        Validate password strength requirements.
        """
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        # Check for at least one uppercase letter
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")

        # Check for at least one lowercase letter
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")

        # Check for at least one digit
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")

        return v


class UserResponse(BaseModel):
    """
    DTO for user response (without sensitive data).
    """

    user_id: int = Field(..., description="User's unique identifier")
    user_name: str = Field(..., description="User's display name")
    email: Optional[EmailStr] = Field(None, description="User's email address")
    refresh_token: str = Field(..., description="User's refresh token")
    is_active: bool = Field(..., description="User's active status")
    is_superuser: bool = Field(..., description="User's superuser status")

    class Config:
        from_attributes = True

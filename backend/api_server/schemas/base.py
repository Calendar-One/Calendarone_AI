from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """
    Global response class for all API returns.
    """

    isError: bool = Field(
        default=False, description="Indicates if the response contains an error"
    )
    message: str = Field(
        ...,
        description="Response message, default is Success, if have error, message is error message",
    )
    data: Optional[T] = Field(default=None, description="Response data")
    errors: Optional[List[str]] = Field(
        default=None, description="Response errors details"
    )

    @classmethod
    def success(
        cls, message: str = "Success", data: Optional[T] = None
    ) -> "ApiResponse[T]":
        """
        Create a successful response.
        """
        return cls(isError=False, message=message, data=data)

    @classmethod
    def error(
        cls,
        message: str = "An error occurred",
        data: Optional[T] = None,
        errors: Optional[List[str]] = None,
    ) -> "ApiResponse[T]":
        """
        Create an error response.
        """
        return cls(isError=True, message=message, data=data, errors=errors)

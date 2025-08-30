# from ast import Tuple
# from api_server.core.config import settings
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt
# from fastapi import Depends, Query, status
# from api_server.core.exceptions import _get_credential_exception

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# def get_pagination_params(
#     skip: int = Query(0, ge=0), limit: int = Query(10, gt=0)
# ) -> Tuple[int, int]:
#     """
#     Get the pagination parameters.

#     Parameters:
#         skip (int): The number of items to skip. Defaults to 0.
#         limit (int): The maximum number of items to return. Defaults to 10.

#     Returns:
#         Tuple[int, int]: A tuple containing the skip and limit values.
#     """
#     return skip, limit


# def get_token(token: str = Depends(oauth2_scheme)) -> TokenPayload:
#     """
#     Retrieve the token payload from the provided JWT token.

#     Parameters:
#         token (str, optional): The JWT token. Defaults to the value returned by the `oauth2_scheme` dependency.

#     Returns:
#         TokenPayload: The decoded token payload.

#     Raises:
#         HTTPException: If there is an error decoding the token or validating the payload.
#     """
#     try:
#         payload = jwt.decode(
#             token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
#         )
#         token_data = TokenPayload(**payload)
#     except (jwt.JWTError, ValidationError) as e:
#         raise _get_credential_exception(status_code=status.HTTP_403_FORBIDDEN) from e
#     return token_data

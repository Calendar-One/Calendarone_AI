from fastapi import APIRouter
from api_server.api.routes import users

from api_server.api.routes import auth


api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)

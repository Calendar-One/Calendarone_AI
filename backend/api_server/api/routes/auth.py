from api_server.schemas import UserLoginRequest
from fastapi import APIRouter

router = APIRouter(tags=["auth"])


@router.post("/login")
async def login(request: UserLoginRequest):
    return {"message": "Login successful"}

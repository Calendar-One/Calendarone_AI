from api_server.api.mian import api_router
from api_server.schemas.base import ApiResponse
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from api_server.core.config import settings
from api_server.core.log import get_logger
from api_server.initial_data import init

from starlette.middleware.cors import CORSMiddleware

log = get_logger(__name__)

# init database
init()

app = FastAPI(
    title="API Server",
    description="FastAPI application",
    version=settings.API_VERSION,
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse[None](
            isError=True,
            message=exc.detail if isinstance(exc.detail, str) else "An error occurred",
            data=None,
            errors=[exc.detail] if isinstance(exc.detail, str) else exc.detail,
        ).model_dump(),
    )


# Set all CORS enabled origins
if settings.ALLOWED_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix="/" + settings.API_VERSION)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World", "version": settings.API_VERSION}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": settings.ENV}

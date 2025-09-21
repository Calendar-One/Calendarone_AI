from api_server.api.mian import api_router
from api_server.schemas.base import ApiResponse
from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from api_server.core.config import settings
from api_server.core.log import get_logger
from api_server.initial_data import init
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

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


def_router = APIRouter(tags=["health"])


@def_router.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World", "version": settings.API_VERSION}


@def_router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": settings.ENV}


api_router.include_router(def_router)

app.include_router(api_router, prefix="/" + settings.API_VERSION)


# the order of the middleware is important
# Add global exception handling middleware
# Custom middleware to handle all exceptions properly
class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            log.error(f"Unhandled exception: {exc}")

            # Include more details in development mode
            error_message = "Internal Server Error"
            error_details = ["An unexpected error occurred"]

            if settings.ENV in ["dev", "test", "local"]:
                error_message = str(exc)
                error_details = [str(exc)]

                response_data = ApiResponse[None](
                    isError=True,
                    message=error_message,
                    data=None,
                    errors=error_details,
                ).model_dump()

            return JSONResponse(
                status_code=500,
                content=response_data,
                headers={"Content-Type": "application/json"},
            )


app.add_middleware(GlobalExceptionMiddleware)

# Add CORS middleware LAST to ensure it wraps everything, add after the exception handler
if settings.ALLOWED_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    # Fallback CORS configuration for development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

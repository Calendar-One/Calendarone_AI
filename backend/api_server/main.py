from fastapi import FastAPI
from api_server.core.config import settings
from api_server.core.log import get_logger
from api_server.initial_data import init

log = get_logger(__name__)


init()

app = FastAPI(
    title="API Server",
    description="FastAPI application",
    version=settings.API_VERSION,
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World", "version": settings.API_VERSION}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "environment": settings.ENV}

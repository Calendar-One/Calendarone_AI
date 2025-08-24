from fastapi import FastAPI
from core.config import settings
from core.log import get_logger

log = get_logger(__name__)

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

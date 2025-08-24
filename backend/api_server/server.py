import uvicorn

from api_server.core.config import settings

if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(
        "api_server.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.ENV in ["test", "dev"],
        log_level="debug" if settings.ENV in ["test", "dev"] else None,
    )

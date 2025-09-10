from contextlib import contextmanager
from typing import Generator

from api_server.database.session import SQLALCHEMY_DATABASE_URL, get_local_session
from api_server.core.exceptions import SQLAlchemyException
from api_server.core.log import get_logger
from api_server.core.config import settings

log = get_logger(__name__)


def get_db() -> Generator:  # pragma: no cover
    """
    Returns a generator that yields a database session

    Yields:
        Session: A database session object.

    Raises:
        Exception: If an error occurs while getting the database session.
    """

    log.debug("getting database session")
    echo = settings.ENV == "local" or settings.ENV == "test" or settings.ENV == "dev"
    db = get_local_session(SQLALCHEMY_DATABASE_URL, echo)()
    try:
        yield db
    finally:  # pragma: no cover
        log.debug("closing database session")
        db.close()  # pragma: no cover


@contextmanager
def get_ctx_db(database_url: str) -> Generator:
    """
    Context manager that creates a database session and yields
    it for use in a 'with' statement.

    Parameters:
        database_url (str): The URL of the database to connect to.

    Yields:
        Generator: A database session.

    Raises:
        Exception: If an error occurs while getting the database session.

    """
    log.debug("getting database session")
    echo = settings.ENV == "local" or settings.ENV == "test" or settings.ENV == "dev"
    db = get_local_session(database_url, echo)()
    try:
        yield db
    except Exception as e:
        log.error("An error occurred while getting the database session. Error: %s", e)
        raise SQLAlchemyException from e
    finally:
        log.debug("closing database session")
        db.close()

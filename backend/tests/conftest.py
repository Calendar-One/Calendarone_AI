
from sqlalchemy import create_engine
from api_server.core.log import get_logger
from api_server.database import SQLALCHEMY_DATABASE_URL
from sqlalchemy.orm import sessionmaker
from api_server.core.config import get_settings
import pytest

log = get_logger()


_test_settings = get_settings("test")


print(SQLALCHEMY_DATABASE_URL)

@pytest.fixture
def test_sqlalchemy_database_url():
    return SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)


@pytest.fixture
def _engine():
    return engine


# @pytest.fixture
# def _test_session(_engine):
#     return sessionmaker(bind=_engine, autocommit=False, autoflush=False)


@pytest.fixture
def test_db_session(_engine):
    log.debug("getting test database session")
    db = sessionmaker(bind=_engine, autocommit=False, autoflush=False)()
    try:
        yield db
    finally:
        log.debug("closing test database session")
        db.close()


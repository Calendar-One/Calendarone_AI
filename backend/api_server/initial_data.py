from api_server.core.log import get_logger
from api_server.database import get_db
from api_server.database import init_db

log = get_logger(__name__)


def init() -> None:
    db_generator = get_db()
    session = next(db_generator)

    try:
        init_db(session)
    finally:
        next(db_generator, None)


def main() -> None:
    log.info("Creating initial data")
    init()
    log.info("Initial data created")


if __name__ == "__main__":
    main()

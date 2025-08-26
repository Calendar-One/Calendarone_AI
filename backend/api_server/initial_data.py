from api_server.core.log import get_logger
from api_server.database import get_db
from api_server.models.users import User

log = get_logger(__name__)


def init() -> None:
    db_generator = get_db()
    session = next(db_generator)

    try:
        user = session.query(User).filter(User.email == "admin@example.com").first()
        if not user:
            import uuid

            user_in = User(
                user_id=str(uuid.uuid4()),
                user_name="admin",
                email="admin@example.com",
                password="admin",
            )
            session.add(user_in)
            session.commit()
        else:
            #  delete user
            session.delete(user)
            session.commit()
    finally:
        session.close()


def main() -> None:
    log.info("Creating initial data")
    init()
    log.info("Initial data created")


if __name__ == "__main__":
    main()

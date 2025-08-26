from sqlalchemy import create_engine, event, false
from sqlalchemy import orm
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from api_server.core.config import Settings, settings
from api_server.models.base import BaseModel


def build_sqlalchemy_database_url_from_settings(_settings: Settings) -> str:
    """
    Builds a SQLAlchemy URL based on the provided settings.

    Parameters:
        _settings (Settings): An instance of the Settings class
        containing the SQL Server connection details.

    Returns:
        str: The generated SQLAlchemy URL for SQL Server using pyodbc.
    """

    # Note: special characters (@, %, !, etc.) in passwords must be URL-encoded.
    # For example, @ → %40.
    from urllib.parse import quote_plus

    encoded_user = quote_plus(_settings.DB_USER)
    encoded_password = quote_plus(_settings.DB_PASSWORD)

    return (
        f"mssql+pyodbc://{encoded_user}:{encoded_password}"
        f"@{_settings.DB_HOST}:{_settings.DB_PORT}/{_settings.DB_NAME}"
        f"?driver=ODBC+Driver+17+for+SQL+Server"
    )


def get_engine(database_url: str, echo=False) -> Engine:
    """
    Creates and returns a SQLAlchemy Engine object for connecting to a database.

    Parameters:
        database_url (str): The URL of the database to connect to.
        Defaults to SQLALCHEMY_DATABASE_URL.
        echo (bool): Whether or not to enable echoing of SQL statements.
        Defaults to False.

    Returns:
        Engine: A SQLAlchemy Engine object representing the database connection.
    """
    engine = create_engine(database_url, echo=echo)
    return engine


# https://docs.sqlalchemy.org/en/20/_modules/examples/extending_query/filter_public.html
@event.listens_for(Session, "before_flush")
def _soft_delete_listener(session, flush_context, instances):
    """
    Intercepts deletes and converts them to soft deletes.
    """
    # Iterate through all objects marked for deletion in this session
    for obj in session.deleted:
        # Check if the object's class has a 'is_deleted' attribute
        if hasattr(obj, "is_deleted"):
            from datetime import datetime, timezone

            # Prevent the hard delete
            session.expunge(obj)

            # Mark the object as modified to trigger an UPDATE
            session.add(obj)

            # Set the soft-delete attributes
            obj.is_deleted = True
            obj.deleted_at = datetime.now(timezone.utc)


@event.listens_for(Session, "do_orm_execute")
def _add_soft_delete_filter_listener(execute_state):
    """
    Add soft delete filter to session queries.
    This function is called for each new session.
    """
    if (
        execute_state.is_select
        and not execute_state.is_column_load
        and not execute_state.is_relationship_load
    ):
        execute_state.statement = execute_state.statement.options(
            orm.with_loader_criteria(
                BaseModel,
                lambda cls: cls.is_deleted == false(),
                include_aliases=True,
            )
        )


def get_local_session(database_url: str, echo=False, **kwargs) -> sessionmaker:
    """
    Create and return a sessionmaker object for a local database session.

    Parameters:
        database_url (str): The URL of the local database.
        Defaults to `SQLALCHEMY_DATABASE_URL`.
        echo (bool): Whether to echo SQL statements to the console.
        Defaults to `False`.

    Returns:
        sessionmaker: A sessionmaker object configured for the local database session.
    """
    engine = get_engine(database_url, echo)

    # Create session factory with event listener
    session_factory = sessionmaker(
        autocommit=False, autoflush=False, bind=engine, **kwargs
    )

    # Add the soft delete filter to each new session
    # @event.listens_for(session_factory, 'after_create')
    # def receive_after_create(session, context):
    #     _add_soft_delete_filter(session)

    return session_factory


SQLALCHEMY_DATABASE_URL = build_sqlalchemy_database_url_from_settings(settings)

from api_server.core.util import get_attribute_as_string
from api_server.models.audit import AuditEntry, AuditEntryProperty
from api_server.core.constant import AuditState
from sqlalchemy import create_engine, event, false
from sqlalchemy import orm
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from api_server.core.config import Settings, settings
from api_server.models.base import BaseModel
from api_server.models.users import User
from sqlalchemy.orm.attributes import get_history
from datetime import datetime, timezone


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


# Session events
@event.listens_for(Session, "before_flush")
def _soft_delete_listener(session, flush_context, instances):
    """
    Intercepts deletes and converts them to soft deletes.
    doc: https://docs.sqlalchemy.org/en/20/orm/events.html#sqlalchemy.orm.SessionEvents.before_flush
    """

    # audit tracker before soft delete
    # audit_tracker(session)
    for obj in session.new:
        if hasattr(obj, "version"):
            if obj.version is None:
                obj.version = 1
            else:
                obj.version += 1

        if hasattr(obj, "created_at"):
            obj.created_date = datetime.now(timezone.utc)

        if hasattr(obj, "created_by"):
            obj.created_by = None

    for obj in session.dirty:
        if hasattr(obj, "version"):
            if obj.version is None:
                obj.version = 1
            else:
                obj.version += 1

        if hasattr(obj, "updated_at"):
            obj.created_date = datetime.now(timezone.utc)

        if hasattr(obj, "updated_by"):
            obj.created_by = None

    # Iterate through all objects marked for deletion in this session
    for obj in session.deleted:
        # Check if the object's class has a 'is_deleted' attribute
        if hasattr(obj, "is_deleted"):
            # Prevent the hard delete
            session.expunge(obj)
            # Mark the object as modified to trigger an UPDATE
            session.add(obj)

            # Set the soft-delete attributes
            if hasattr(obj, "deleted_at"):
                obj.deleted_at = datetime.now(timezone.utc)

            if hasattr(obj, "deleted_by"):
                obj.deleted_by = None

            if hasattr(obj, "is_deleted"):
                obj.is_deleted = True

            if hasattr(obj, "version"):
                if obj.version is None:
                    obj.version = 1
                else:
                    obj.version += 1


def audit_tracker(session: Session):
    """
    Manually check and log changes for a specific model instance.
    Call this before committing changes.
    """
    for obj in session.new:
        if isinstance(obj, AuditEntry):
            continue
        if isinstance(obj, AuditEntryProperty):
            continue
        auditEntry = AuditEntry(
            created_by=obj.created_by,
            created_date=obj.created_at,
            entity_set_name=obj.__tablename__,
            entity_type_name=obj.__class__.__name__,
            state=AuditState.ENTITY_ADDED.value,
            state_name=AuditState.ENTITY_ADDED.label,
        )
        auditEntry.properties = []

        mapper = obj.__mapper__
        for column in mapper.columns:
            attr_name = column.name
            old_value = None
            new_value = get_attribute_as_string(obj, attr_name)

            auditEntryProperty = AuditEntryProperty(
                property_name=attr_name,
                old_value=old_value,
                new_value=new_value,
            )
            auditEntry.properties.append(auditEntryProperty)
        session.add(auditEntry)

    for obj in session.dirty:
        if isinstance(obj, AuditEntry):
            continue
        if isinstance(obj, AuditEntryProperty):
            continue

        mapper = obj.__mapper__
        primary_key_columns = [col.name for col in mapper.primary_key]

        # check if the object is deleted
        if hasattr(obj, "is_deleted") and obj.is_deleted:
            auditEntry = AuditEntry(
                created_by=obj.deleted_by,
                created_date=obj.deleted_at,
                entity_set_name=obj.__tablename__,
                entity_type_name=obj.__class__.__name__,
                state=AuditState.ENTITY_DELETED.value,
                state_name=AuditState.ENTITY_DELETED.label,
            )

            for column in mapper.columns:
                attr_name = column.name
                old_value = get_attribute_as_string(obj, attr_name)
                new_value = None

                auditEntryProperty = AuditEntryProperty(
                    property_name=attr_name,
                    old_value=old_value,
                    new_value=new_value,
                )
                auditEntry.properties.append(auditEntryProperty)
            session.add(auditEntry)

        else:
            auditEntry = AuditEntry(
                created_by=obj.updated_by,
                created_date=obj.updated_at,
                entity_set_name=obj.__tablename__,
                entity_type_name=obj.__class__.__name__,
                state=AuditState.ENTITY_MODIFIED.value,
                state_name=AuditState.ENTITY_MODIFIED.label,
            )
            auditEntry.properties = []
            mapper = obj.__mapper__

            for column in mapper.columns:
                attr_name = column.name
                history = get_history(obj, attr_name)

                if history.has_changes():
                    old_value = history.deleted[0] if history.deleted else None
                    new_value = (
                        history.added[0]
                        if history.added
                        else get_attribute_as_string(obj, attr_name)
                    )
                    auditEntryProperty = AuditEntryProperty(
                        property_name=attr_name,
                        old_value=old_value,
                        new_value=new_value,
                    )
                    auditEntry.properties.append(auditEntryProperty)
                elif (
                    attr_name in primary_key_columns
                ):  # only track primary key columns for audit for unchanged columns
                    old_value = get_attribute_as_string(obj, attr_name)
                    new_value = old_value
                    auditEntryProperty = AuditEntryProperty(
                        property_name=attr_name,
                        old_value=old_value,
                        new_value=new_value,
                    )
                    auditEntry.properties.append(auditEntryProperty)

            session.add(auditEntry)

    for obj in session.deleted:
        if isinstance(obj, AuditEntry):
            continue
        if isinstance(obj, AuditEntryProperty):
            continue
        auditEntry = AuditEntry(
            created_by=obj.deleted_by,
            created_date=obj.deleted_at,
            entity_set_name=obj.__tablename__,
            entity_type_name=obj.__class__.__name__,
            state=AuditState.ENTITY_DELETED.value,
            state_name=AuditState.ENTITY_DELETED.label,
        )

        mapper = obj.__mapper__
        for column in mapper.columns:
            attr_name = column.name
            old_value = get_attribute_as_string(obj, attr_name)
            new_value = None

            auditEntryProperty = AuditEntryProperty(
                property_name=attr_name,
                old_value=old_value,
                new_value=new_value,
            )
            auditEntry.properties.append(auditEntryProperty)
        session.add(auditEntry)


@event.listens_for(Session, "after_flush")
def db_after_flush(session, flush_context):
    # audit tracker after flush
    audit_tracker(session)


@event.listens_for(Session, "do_orm_execute")
def _add_soft_delete_filter_listener(execute_state):
    """
    Add soft delete filter to session queries.
    This function is called for each new session.
    Ref: https://docs.sqlalchemy.org/en/20/_modules/examples/extending_query/filter_public.html
    """
    # state ref => https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.ORMExecuteState
    if (
        execute_state.is_select
        and not execute_state.is_column_load
        and not execute_state.is_relationship_load
    ):
        execute_state.statement = execute_state.statement.options(
            orm.with_loader_criteria(
                BaseModel,
                lambda cls: cls.is_deleted == false()
                if hasattr(cls, "is_deleted")
                else True,
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


# init data
def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from app.models
    # SQLModel.metadata.create_all(engine)

    user = (
        session.query(User).filter(User.email == settings.FIRST_SUPERUSER_EMAIL).first()
    )
    if not user:
        user_in = User(
            user_name=settings.FIRST_SUPERUSER_USERNAME,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
        )
        session.add(user_in)
        session.commit()

    user = (
        session.query(User).filter(User.email == settings.FIRST_SUPERUSER_EMAIL).first()
    )
    if user:
        user.user_name = "eeeee"
        session.commit()

    user = (
        session.query(User).filter(User.email == settings.FIRST_SUPERUSER_EMAIL).first()
    )
    if user:
        session.delete(user)
        session.commit()

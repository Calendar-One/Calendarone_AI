import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env.dev", env_file_encoding="utf-8", case_sensitive=True
    )

    API_VERSION: str
    ENV: str

    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int

    SERVER_HOST: str
    SERVER_PORT: int

    LOG_FILE_ROTATION_DAYS: int
    LOG_FILE_PATH: str


def get_env_file_parent_path() -> str:
    cwd = os.getcwd()
    if cwd.endswith("backend"):
        return "./"
    if cwd.endswith("api_server"):
        return "../"
    return "./"


class ContainerDevSettings(Settings):
    model_config = SettingsConfigDict(
        env_file=get_env_file_parent_path() + ".env.dev",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    ENV: str = "dev"


class ContainerTestSettings(Settings):
    model_config = SettingsConfigDict(
        env_file=get_env_file_parent_path() + ".env.test",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    ENV: str = "test"


class LocalTestSettings(Settings):
    model_config = SettingsConfigDict(
        env_file=get_env_file_parent_path() + ".env.test.local",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    ENV: str = "test"


class LocalDevSettings(Settings):
    model_config = SettingsConfigDict(
        env_file=get_env_file_parent_path() + ".env.local",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    ENV: str = "local"


def get_settings(env: str = "dev") -> Settings:
    """
    Return the settings object based on the environment.

    Parameters:
        env (str): The environment to retrieve the settings for. Defaults to "dev".

    Returns:
        Settings: The settings object based on the environment.

    Raises:
        ValueError: If the environment is invalid.
    """

    if env.lower() in ["dev", "d", "development"]:
        return ContainerDevSettings()
    if env.lower() in ["test", "t", "testing"]:
        return ContainerTestSettings()
    if env.lower() in ["local", "l"]:
        return LocalDevSettings()

    raise ValueError("Invalid environment. Must be 'dev' or 'test' ,'local'.")


_env = os.environ.get("ENV", "dev")

settings = get_settings(env=_env)

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from loguru import Logger

import os
from typing import Optional
from loguru import logger

import sys
from api_server.core.config import settings


# Define valid debug levels
DebugLevels = ["DEBUG", "INFO", "WARNING", "ERROR"]
DebugLevelType = str


def get_logger(
    name: Optional[str] = None,
    log_file: Optional[str] = None,
    level: DebugLevelType = "DEBUG",
) -> Logger:
    """
    Creates and configures a logger for logging messages using loguru.

    Parameters:
        name (Optional[str]): The name/context for the logger. Defaults to None.
        level (DebugLevelType): The logging level. Defaults to "DEBUG".

    Returns:
        loguru.Logger: The configured logger object.
    """
    # Remove default handler to avoid duplicate logs
    logger.remove()

    # Validate logging level
    if not level or level not in DebugLevels:
        # Add a temporary handler to log the warning
        logger.add(
            sys.stdout,
            format="{time:YYYY-MM-DD HH:mm:ss} - {name} - {level} - {message}",
            level="WARNING",
        )
        logger.warning(
            f"Invalid logging level {level}. Setting logging level to DEBUG."
        )
        level = "DEBUG"
        logger.remove()  # Remove the temporary handler

    # Configure the logger with custom format
    log_format = "{time:YYYY-MM-DD HH:mm:ss} - {name} - {level} - {message}"

    # Add handler with specified level and format
    if log_file:
        if not log_file.endswith(".log"):
            log_file = f"{log_file}.log"
        if not os.path.isabs(log_file):
            # Convert relative log file path to absolute path using the configured LOG_FILE_PATH
            # settings.LOG_FILE_PATH is the base directory for log files from config
            # log_file is the filename (e.g., "app.log")
            # The / operator creates a Path object, and resolve() converts it to absolute path
            log_file = str((settings.LOG_FILE_PATH / log_file).resolve())
        logger.add(
            log_file,
            format=log_format,
            level=level,
            colorize=True,
        )
    else:
        logger.add(
            sys.stdout,
            format=log_format,
            level=level,
            colorize=True,  # Optional: adds colors to log levels
        )

    # If a specific name is provided, bind it to the logger context
    if name:
        return logger.bind(name=name)

    return logger

from enum import Enum, StrEnum

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class CommonConfig(StrEnum):
    """Common configuration."""

    ENV_PREFIX = "PDF_SUMMARY_AI__"
    """Prefix for environment variables"""
    ENV_NESTED_DELIMITER = "__"
    """Delimiter for environment variables"""
    VERSION_FILE_NAME = "VERSION"
    """Name of version file"""


class ProjectAbout(BaseModel):
    """Project about."""

    name: str
    """Project name"""
    version: str
    """Project version"""
    description: str
    """Project description"""


class LoggingSettings(BaseModel):
    """Base configuration for logging."""

    app_log_level: str = "INFO"
    """Logging level"""


class ServiceSettings(BaseModel):
    """The main service configuration."""

    mode: str
    """DEV or PROD"""
    name: str | None = None
    """Name of the service"""
    description: str | None = None
    """Description of the service"""
    root_path: str = ""
    """The root path to the service"""
    host: str = "0.0.0.0"
    """The host of the service"""
    port: int = 8080
    """The port to connect to service"""
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    """The service logging settings"""

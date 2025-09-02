from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config.base import CommonConfig, ServiceSettings

# from src.config.external import ExternalSettings


class Config(BaseSettings):
    """Main configuration class."""

    model_config = SettingsConfigDict(
        env_prefix=CommonConfig.ENV_PREFIX,
        env_nested_delimiter=CommonConfig.ENV_NESTED_DELIMITER,
        case_sensitive=False,
    )

    service_settings: ServiceSettings = Field(default_factory=ServiceSettings)

    # external_services_settings: ExternalSettings = Field(
    #     default_factory=ExternalSettings
    # )

    version: str

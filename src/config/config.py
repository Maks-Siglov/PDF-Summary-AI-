from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config.base import CommonConfig, ServiceSettings
from src.config.openai import OpenAISettings
from src.config.pdf import PDFSettings


class Config(BaseSettings):
    """Main configuration class."""

    model_config = SettingsConfigDict(
        env_prefix=CommonConfig.ENV_PREFIX,
        env_nested_delimiter=CommonConfig.ENV_NESTED_DELIMITER,
        case_sensitive=False,
    )

    service_settings: ServiceSettings = Field(default_factory=ServiceSettings)

    pdf_settings: PDFSettings = Field(default_factory=PDFSettings)

    openai_settings: OpenAISettings = Field(default_factory=OpenAISettings)

    version: str

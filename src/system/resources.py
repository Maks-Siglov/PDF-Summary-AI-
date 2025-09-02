from dependency_injector import containers, providers
from dependency_injector.containers import WiringConfiguration
from fastapi import FastAPI

from src.client.openai import OpenAIClient
from src.config.config import Config
from src.prompt.system import SYSTEM_PROMPT
from src.services.pdf.summary import PDFSummaryService


class IoCContainer(containers.DeclarativeContainer):

    wiring_config = WiringConfiguration(packages=["src.api"])

    config: Config = providers.Configuration()

    # CLIENTS

    openai_client: OpenAIClient = providers.Singleton(
        OpenAIClient,
        api_key=config.openai_settings.api_key,
        system_prompt=SYSTEM_PROMPT,
        model=config.openai_settings.model,
        temperature=config.openai_settings.temperature,
    )

    # SERVICES

    pdf_summary_service: PDFSummaryService = providers.Singleton(
        PDFSummaryService, file_size_mb_limit=config.pdf_settings.size_mb_limit
    )


async def startup_event(app: FastAPI) -> None:
    """Initialize resources.

    Args:
        app (FastAPI): The application.
    """
    if app.state.container.init_resources() is not None:
        await app.state.container.init_resources()


async def shutdown_event(app: FastAPI) -> None:
    """Clean all allocated resources.

    Args:
        app (FastAPI): The application.
    """
    if app.state.container.init_resources() is not None:
        await app.state.container.shutdown_resources()

from dependency_injector import containers, providers
from dependency_injector.containers import WiringConfiguration
from fastapi import FastAPI

from src.config.config import Config
from src.services.pdf.summary import PDFSummaryService


class IoCContainer(containers.DeclarativeContainer):

    wiring_config = WiringConfiguration(packages=["src.api"])

    config: Config = providers.Configuration()

    # SERVICES

    pdf_summary_service: PDFSummaryService = providers.Singleton(
        PDFSummaryService,
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

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from loguru import logger

from src.api.v1 import setup_routes
from src.config.config import Config
from src.core.models.enums import ServiceLaunchMode
from src.system.middlewares import setup_middlewares
from src.system.resources import IoCContainer, shutdown_event, startup_event


def custom_openapi(app: FastAPI, config: Config) -> dict[str, Any]:
    """OpenAPI configuration.

    Args:
        app (FastAPI): FastAPI application.
        config (Config): Application configuration.

    Returns:
        dict[str, Any]: OpenAPI schema.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=config.service_settings.name,
        version=config.version,
        description=config.service_settings.description,
        routes=app.routes,
    )

    # look for the error 422 and removes it
    # (default ValidationError response schema)
    for method in openapi_schema["paths"]:
        try:
            del openapi_schema["paths"][method]["post"]["responses"]["422"]
            del openapi_schema["paths"][method]["get"]["responses"]["422"]
        except KeyError:
            pass

    app.openapi_schema = openapi_schema
    return app.openapi_schema


def prepare_app(config: Config) -> FastAPI:
    """Prepare the application.

    Args:
        config (Config): The application configuration.

    Returns:
        FastAPI: The application.
    """

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Startup events
        await startup_event(app)
        yield
        # Shutdown events
        await shutdown_event(app)

    if config.service_settings.mode == ServiceLaunchMode.DEV:
        app = FastAPI(
            root_path=config.service_settings.root_path,
            lifespan=lifespan,
        )
    else:
        app = FastAPI(
            root_path=config.service_settings.root_path,
            lifespan=lifespan,
            docs_url=None,
            redoc_url=None,
        )

    container = IoCContainer()
    container.config.from_dict(config.model_dump())
    app.state.container = container

    setup_routes(app)
    setup_middlewares(app)

    app.openapi_schema = custom_openapi(app, config)

    logger.info("Service is set up")
    return app

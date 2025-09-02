from fastapi import APIRouter, FastAPI

from .pdf import router as pdf_summary_router


def setup_routes(app: FastAPI) -> None:
    """Set up the API routes.

    Args:
        app (FastAPI): The FastAPI application.
    """
    router = APIRouter(prefix="/api/v1")

    router.include_router(pdf_summary_router)

    app.include_router(router)

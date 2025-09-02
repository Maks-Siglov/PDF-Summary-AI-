import traceback
from json import JSONDecodeError

from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from loguru import logger
from starlette.responses import JSONResponse

from src.core.schemas.responses import ErrorResponse


async def http_exception_handler(
    _: Request, exc: HTTPException
) -> JSONResponse:
    """Handles HTTP exceptions.

    Args:
        _ (Request): Request.
        exc (HTTPException): HTTP exception.

    Returns:
        JSONResponse: Response for the exception.
    """
    logger.error(f"ERROR handled by http_exception_handler: {exc}")
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            e_name=exc.status_code,
            e_message=exc.detail,
        ).model_dump(),
        headers=exc.headers,
    )


async def value_error_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    """Handles value exceptions.

    Args:
        request (Request): Request.
        exc (Exception): Exception.

    Returns:
        JSONResponse: Response for the exception.
    """
    logger.error(
        f"ERROR handled by value_error_handler: 400 Bad Request: {exc}"
    )
    try:
        body = await request.json()
        logger.error(f"Request body: {body}")
    except (ValueError, JSONDecodeError):
        logger.error("Could not parse request body")

    logger.error(f"Request query params: {request.query_params}")

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponse(
            e_name="Bad Request",
            e_message=str(exc),
        ).model_dump(),
    )


async def common_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    """Handles common exceptions.

    Args:
        _ (Request): Request.
        exc (Exception): Exception.

    Returns:
        JSONResponse: Response for the exception.
    """
    traceback.print_stack()
    traceback.print_exc()
    logger.error(f"ERROR handled by common_exception_handler: 500: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            e_name="Internal Server Error",
            e_message=str(exc),
        ).model_dump(),
    )


def add_error_handler_middleware(app: FastAPI) -> None:
    """Handles application errors.

    Args:
        app (FastAPI): Application.
    """
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(ValueError, value_error_handler)
    app.add_exception_handler(RequestValidationError, value_error_handler)
    app.add_exception_handler(Exception, common_exception_handler)


def setup_middlewares(app: FastAPI) -> None:
    """Setups a middleware for application.

    Args:
        app (FastAPI): Application.
    """
    add_error_handler_middleware(app)

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, Response, UploadFile

from src.core.exceptions import (
    EmptyFileException,
    TooLargeFileException,
    WrongFileFormatException,
)
from src.services.pdf.summary import PDFSummaryService
from src.system.resources import IoCContainer


router = APIRouter(prefix="/pdf")


@router.post("/summary")
@inject
async def summary_pdf(
    file: UploadFile = File(...),
    pdf_summary_service: PDFSummaryService = Depends(
        Provide[IoCContainer.pdf_summary_service]
    ),
) -> Response:
    """Upload and process PDF file."""

    try:
        await pdf_summary_service.get_pdf_summary(file)
    except WrongFileFormatException:
        return Response(status_code=400, content="Only PDF files are allowed")
    except TooLargeFileException:
        return Response(status_code=400, content="PDF file is too large")
    except EmptyFileException:
        return Response(
            status_code=200, content="There is no summary for empty PDF"
        )

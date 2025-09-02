import io

import pdfplumber
from fastapi import UploadFile

from src.core.exceptions import (
    EmptyFileException,
    TooLargeFileException,
    WrongFileFormatException,
)


class PDFSummaryService:

    def __init__(self, file_size_mb_limit: int):
        self._file_size_mb_limit = file_size_mb_limit

    async def get_pdf_summary(self, file: UploadFile):

        if not file.filename.lower().endswith(".pdf"):
            raise WrongFileFormatException()

        if file.size and file.size > self._file_size_mb_limit * 1024 * 1024:
            raise TooLargeFileException()

        content = await file.read()
        text_content, page_count = self.extract_text_from_pdf(content)

        if not text_content.strip():
            raise EmptyFileException()

    @staticmethod
    def extract_text_from_pdf(pdf_content: bytes) -> str:
        """Extract text from PDF including handling of images and tables."""
        text_content = []

        with io.BytesIO(pdf_content) as pdf_file:
            with pdfplumber.open(pdf_file) as pdf:

                for page_num, page in enumerate(pdf.pages):
                    # Extract text
                    text = page.extract_text()
                    if text:
                        text_content.append(
                            f"--- Page {page_num + 1} ---\n{text}"
                        )

                    # Extract tables if present
                    tables = page.extract_tables()
                    for table_num, table in enumerate(tables):
                        table_text = (
                            f"\n--- Table {table_num + 1} on Page"
                            f" {page_num + 1} ---\n"
                        )
                        for row in table:
                            if row:
                                table_text += (
                                    " | ".join([cell or "" for cell in row])
                                    + "\n"
                                )
                        text_content.append(table_text)

        full_text = "\n\n".join(text_content)
        return full_text

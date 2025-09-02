from pydantic import BaseModel


class PDFSettings(BaseModel):
    size_mb_limit: int

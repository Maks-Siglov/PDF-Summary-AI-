from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Error response schema."""

    e_name: str
    """The name of the error"""
    e_message: str
    """The message of the error"""

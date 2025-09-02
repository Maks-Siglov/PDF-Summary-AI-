from uuid import UUID

from pydantic import BaseModel


class SendMessageModel(BaseModel):
    """Schema for chat service."""

    user_id: str
    session_id: UUID
    query: str

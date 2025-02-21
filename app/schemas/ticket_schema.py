from pydantic import BaseModel
from typing import Optional

class TicketSchema(BaseModel):
    title: str
    description: str
    status: Optional[str] = "open"

    class Config:
        orm_mode = True

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    assignee_id: Optional[str] = None

class TicketResponse(BaseModel):
    id: str
    title: str
    description: str
    status: str
    assignee_id: str

    class Config:
        orm_mode = True




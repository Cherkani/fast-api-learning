from pydantic import BaseModel
from typing import Optional

class TicketSchema(BaseModel):
    title: str
    description: str
    status: Optional[str] = "open"

    class Config:
        orm_mode = True

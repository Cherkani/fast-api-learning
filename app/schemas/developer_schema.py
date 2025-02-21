from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .ticket_schema import TicketSchema

class DeveloperSchema(BaseModel):
    name: str
    email: EmailStr
    level: Optional[str]

    class Config:
        orm_mode = True

class DeveloperWithTicketsSchema(DeveloperSchema):
    tickets: List[TicketSchema] = []

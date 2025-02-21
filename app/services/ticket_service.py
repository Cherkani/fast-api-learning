from sqlalchemy.orm import Session
from ..models.ticket import Ticket
from ..models.developer import Developer
from ..schemas.ticket_schema import TicketSchema

class TicketService:
    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, ticket: TicketSchema, developer_id: str):
        developer = self.db.query(Developer).filter(Developer.id == developer_id).first()
        if not developer:
            raise ValueError("Developer not found")
        
        new_ticket = Ticket(**ticket.dict(), assignee_id=developer_id)
        self.db.add(new_ticket)
        self.db.commit()
        self.db.refresh(new_ticket)
        return new_ticket

    def get_all_tickets(self):
        return self.db.query(Ticket).all()

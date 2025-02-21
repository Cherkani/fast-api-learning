from sqlalchemy.orm import Session
from ..models.ticket import Ticket
from ..models.developer import Developer
from ..schemas.ticket_schema import TicketSchema, TicketUpdate

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

    def update_ticket(self, ticket_id: str, ticket_update: TicketUpdate):
        ticket = self.db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            raise ValueError(f"Ticket with id {ticket_id} not found")
        
        if ticket_update.assignee_id:
            clean_assignee_id = ticket_update.assignee_id.strip('"\'')
            new_assignee = self.db.query(Developer).filter(Developer.id == clean_assignee_id).first()
            if not new_assignee:
                raise ValueError(f"Developer with id {clean_assignee_id} not found")
            ticket_update.assignee_id = clean_assignee_id

        update_data = ticket_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                setattr(ticket, field, value)

        self.db.commit()
        self.db.refresh(ticket)
        return ticket

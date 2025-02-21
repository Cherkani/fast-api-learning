from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..services.ticket_service import TicketService
from ..schemas.ticket_schema import TicketSchema, TicketUpdate, TicketResponse
from ..db.database import get_db
from ..utils.response_wrapper import api_response

router = APIRouter()

@router.post("/developers/{developer_id}/tickets")
def create_ticket(developer_id: str, ticket: TicketSchema, db: Session = Depends(get_db)):
    service = TicketService(db)
    try:
        clean_developer_id = developer_id.strip("'\"")
        new_ticket = service.create_ticket(ticket, clean_developer_id)
        return api_response(data=new_ticket, message="Ticket created successfully")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("")
def get_all_tickets(db: Session = Depends(get_db)):
    service = TicketService(db)
    tickets = service.get_all_tickets()
    return api_response(data=tickets, message="Tickets retrieved successfully")

@router.put("/{ticket_id}")
def update_ticket(ticket_id: str, ticket_update: TicketUpdate, db: Session = Depends(get_db)):
    service = TicketService(db)
    try:
        # Clean the ticket_id by removing quotes
        cleaned_ticket_id = ticket_id.strip('"\'')
        updated_ticket = service.update_ticket(cleaned_ticket_id, ticket_update)
        # Return the ticket directly without using api_response wrapper
        return updated_ticket
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

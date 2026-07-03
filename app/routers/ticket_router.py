from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import TicketCreate, TicketResponse
from app.services import ticket_service
import uuid

router = APIRouter()


@router.post("/tickets", response_model=TicketResponse)
def criar_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return ticket_service.criar_ticket(ticket, db)

@router.get("/tickets", response_model=list[TicketResponse])
def listar_tickets(db: Session = Depends(get_db)):
    return ticket_service.listar_tickets(db)
    
@router.patch("/tickets/{ticket_id}/status", response_model= TicketResponse)
def atualizar_status_ticket(ticket_id: uuid.UUID, novo_status: str, db: Session = Depends(get_db)):
        return ticket_service.atualizar_status_ticket(ticket_id, novo_status, db)

@router.delete("/tickets/{ticket_id}", response_model=TicketResponse)
def deletar_ticket(ticket_id: uuid.UUID, db: Session = Depends(get_db)):
    return ticket_service.deletar_ticket(ticket_id, db)
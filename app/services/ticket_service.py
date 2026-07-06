import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import Ticket
from app.repositories import ticket_repository
from app.schemas.schemas import TicketCreate


def criar_ticket(ticket: TicketCreate, db: Session):
    novo_ticket = Ticket(**ticket.model_dump())
    return ticket_repository.salvar(novo_ticket, db)

def buscar_ticket_por_id(ticket_id: uuid.UUID, db: Session):
    ticket = ticket_repository.buscar_por_id(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket não encontrado")
    
    return ticket

def atualizar_status_ticket(ticket_id: uuid.UUID, novo_status: str, db: Session):
    ticket = ticket_repository.buscar_por_id(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket não encontrado")
    
    ticket.status = novo_status
    return ticket_repository.atualizar(ticket, db)

def deletar_ticket(ticket_id: uuid.UUID, db: Session):
    ticket = ticket_repository.buscar_por_id(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket não encontrado")
    
    return ticket_repository.deletar(ticket, db)
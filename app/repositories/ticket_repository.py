import uuid

from sqlalchemy.orm import Session
from app.models.models import Ticket


def salvar(ticket: Ticket, db: Session) -> Ticket:
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def listar_tickets(db: Session) -> list[Ticket]:
    return db.query(Ticket).all()

def buscar_por_id(db: Session, ticket_id: uuid.UUID) -> Ticket | None:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def atualizar(ticket: Ticket, db: Session) -> Ticket:
    db.commit()
    db.refresh(ticket)
    return ticket

def deletar(ticket: Ticket, db: Session)  -> Ticket:
    db.delete(ticket)
    db.commit()
    return ticket
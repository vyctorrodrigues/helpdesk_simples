from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.models import Ticket
from schemas.schemas import TicketCreate, TicketResponse
from models.users import User
from routers.auth_router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tickets", response_model=TicketResponse)
def criar_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    novo_ticket = Ticket(**ticket.model_dump())
    db.add(novo_ticket)
    db.commit()
    db.refresh(novo_ticket)
    return novo_ticket

@app.get("/tickets", response_model=list[TicketResponse])
def listar_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@app.patch("/tickets/{ticket_id}/status", response_model= TicketResponse)
def atualizar_status_ticket(ticket_id: int, novo_status: str, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail= "Ticket não encontrado")
    ticket.status = novo_status
    db.commit()
    db.refresh(ticket)
    return ticket

@app.delete("/tickets/{ticket_id}", response_model=TicketResponse)
def deletar_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=204, detail="Ticket não encontrado")
    db.delete(ticket)
    db.commit()
    return ticket
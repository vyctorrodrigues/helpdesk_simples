import uuid
from sqlalchemy import UUID, Column, String, DateTime
from app.database import Base
import datetime


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nome_empresa = Column(String, nullable=False)
    nome_pessoa = Column(String, nullable=False)
    local = Column(String, nullable=False)
    data_hora = Column(DateTime, default=datetime.datetime.now)
    descricao = Column(String, nullable=False)
    status = Column(String, default='Aberto')

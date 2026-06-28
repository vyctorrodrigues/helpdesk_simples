from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    nome_empresa = Column(String, nullable=False)
    nome_pessoa = Column(String, nullable=False)
    local = Column(String, nullable=False)
    data_hora = Column(DateTime, default=datetime.datetime.now)
    descricao = Column(String, nullable=False)
    status = Column(String, default='Aberto')

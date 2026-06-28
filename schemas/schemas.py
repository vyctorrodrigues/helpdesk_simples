from pydantic import BaseModel
from uuid import UUID
import datetime

class TicketCreate(BaseModel):
    nome_empresa: str
    nome_pessoa: str
    local: str
    descricao: str

class TicketResponse(BaseModel):
    id: int
    nome_empresa: str
    nome_pessoa: str
    local: str
    data_hora: datetime.datetime
    descricao: str
    status: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    senha: str

class UserResponse(BaseModel):
    id: UUID
    email: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    acesso_token: str
    token_type: str = "bearer"
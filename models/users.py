from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import uuid



class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
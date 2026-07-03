

from fastapi import FastAPI

from app.database import Base, engine
from app.routers.auth_router import router as auth_router
from app.routers.ticket_router import router as ticket_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ticket_router)
app.include_router(auth_router)

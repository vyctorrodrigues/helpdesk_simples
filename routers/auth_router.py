from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.users import User
from schemas.schemas import UserCreate, UserResponse, TokenResponse
from auth import criptografa_senha, verifica_senha, gerar_token_acesso

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/cadastro", response_model=UserResponse)
def cadastro_usuario(usuario: UserCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(User).filter(User.email == usuario.email.lower()).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    novo_usuario = User(
        email = usuario.email.lower(),
        senha = criptografa_senha(usuario.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@router.post("/auth/login", response_model=TokenResponse)
def login_usuario(usuario: UserCreate, db: Session = Depends(get_db)):

    usuario_existente = db.query(User).filter(User.email == usuario.email.lower()).first()

    if not usuario_existente or not verifica_senha(usuario.senha, usuario_existente.senha):
        raise HTTPException(status_code=401, detail= "Email ou senha inválidos")
    
    token_acesso = gerar_token_acesso({"sub": str(usuario_existente.id)})
    return TokenResponse(acesso_token=token_acesso, token_type="bearer")

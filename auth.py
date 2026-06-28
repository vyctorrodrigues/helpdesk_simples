import bcrypt
from jose import jwt, JWTError
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30

def criptografa_senha(senhas: str) -> str:
    return bcrypt.hashpw(senhas.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verifica_senha(senha: str, hash: str) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hash.encode('utf-8'))

def gerar_token_acesso(dados: dict) -> str:
    payload = dados.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    payload.update({"exp": expiration})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token_acesso(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

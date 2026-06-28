# HelpDesk Simples

API REST para gerenciamento de tickets de suporte técnico, desenvolvida com FastAPI e PostgreSQL.

## 🚀 Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)
- Pydantic
- python-jose
- bcrypt

## 📋 Funcionalidades

- Criar ticket de atendimento
- Listar todos os tickets
- Atualizar status do ticket (aberto, em andamento, fechado)
- Deletar ticket
- Autenticação JWT

## 🖥️ Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /tickets | Criar novo ticket |
| GET | /tickets | Listar todos os tickets |
| PATCH | /tickets/{id}/status | Atualizar status |
| DELETE | /tickets/{id} | Deletar ticket |
| POST | /auth/cadastro | Cadastrar usuário
| POST | /auth/login | Login e geração de token JWT

## 📸 Preview

### Documentação da API
![Swagger](assets/swagger.jpg)

### Banco de dados
![Neon](assets/neon.jpg)

## ⚙️ Como rodar localmente

1. Clone o repositório
2. Instale as dependências
```bash
pip install -r requirements.txt
```
3. Crie um arquivo `.env` na raiz com sua connection string do Neon e também será necessario adicionar SECRET_KEY dentro do arquivo.
```env 
DATABASE_URL=postgresql://usuario:senha@host/banco
```
4. Rode a aplicação
```bash
uvicorn main:app --reload
```
5. Acesse `http://127.0.0.1:8000/docs`

## 👨‍💻 Autor

Vyctor Rodrigues — [GitHub](https://github.com/vyctorrodrigues)
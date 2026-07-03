# 🛠️ HelpDesk Simples

API REST para gerenciamento de tickets de suporte técnico, desenvolvida com **FastAPI**, **SQLAlchemy** e **PostgreSQL**.

Este projeto foi criado com foco em aprendizado de desenvolvimento Back-end utilizando Python, aplicando conceitos de arquitetura em camadas, autenticação JWT e boas práticas de organização de código.

---

# 🚀 Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)
- Pydantic
- Uvicorn
- python-jose (JWT)
- bcrypt

---

# 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas, separando as responsabilidades da aplicação para facilitar manutenção, escalabilidade e organização do código.

```text
Cliente
    │
    ▼
Router
    │
    ▼
Service
    │
    ▼
Repository
    │
    ▼
PostgreSQL
```

### Responsabilidade de cada camada

- **Router:** recebe as requisições HTTP e direciona para a camada de serviço.
- **Service:** contém toda a lógica de negócio da aplicação.
- **Repository:** realiza todas as operações de acesso ao banco de dados.
- **Models:** representam as tabelas do banco.
- **Schemas:** validam os dados de entrada e saída da API.

---

# 📋 Funcionalidades

- ✅ Cadastro de usuários
- ✅ Login utilizando JWT
- ✅ Criação de tickets
- ✅ Listagem de tickets
- ✅ Atualização do status dos tickets
- ✅ Exclusão de tickets
- ✅ Persistência utilizando PostgreSQL (Neon)

---

# 🖥️ Endpoints

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | `/auth/cadastro` | Cadastro de usuário |
| POST | `/auth/login` | Login e geração do token JWT |
| POST | `/tickets` | Criar novo ticket |
| GET | `/tickets` | Listar tickets |
| PATCH | `/tickets/{id}/status` | Atualizar status do ticket |
| DELETE | `/tickets/{id}` | Excluir ticket |

---

# 📂 Estrutura do Projeto

```text
app/
│
├── models/
│   ├── models.py
│   └── users.py
│
├── schemas/
│
├── routers/
│   ├── auth_router.py
│   └── ticket_router.py
│
├── services/
│   └── ticket_service.py
│
├── repositories/
│   └── ticket_repository.py
│
├── auth.py
├── database.py
└── main.py
```

---

# 📸 Preview

## Documentação (Swagger)

![Swagger](assets/swagger.jpg)

## Banco de Dados (Neon)

![Neon](assets/neon.jpg)

---

# ⚙️ Executando o projeto

## Clone o repositório

```bash
git clone https://github.com/vyctorrodrigues/helpdesk_simples.git
```

Entre na pasta do projeto

```bash
cd helpdesk_simples
```

Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto

Copie o arquivo `.env.example` para `.env` e preencha os valores:

```bash
cp .env.example .env

Execute a aplicação

```bash
uvicorn app.main:app --reload
```

Acesse a documentação da API

```
http://127.0.0.1:8000/docs
```

---

# 📈 Próximas melhorias

- Número público para identificação dos tickets
- Comentários em tickets
- Upload de anexos
- Docker
- Alembic (migrações)
- Testes automatizados
- Controle de permissões por usuário

---

# 👨‍💻 Autor

**Vyctor Rodrigues**

Estudante de Análise e Desenvolvimento de Sistemas, apaixonado por desenvolvimento Back-end e arquitetura de software.

GitHub:
https://github.com/vyctorrodrigues
# 💰 Finance API

📋 API REST de gestão financeira pessoal desenvolvida com **FastAPI**, **SQLAlchemy** e **PostgreSQL**.

![Diagrama UML](finance_api_uml_v3.png)

---

## 🛠️ Tecnologias

| Tecnologia | Função |
|---|---|
| Python 3.13 | Linguagem principal |
| FastAPI | Framework web para a API |
| SQLAlchemy | ORM — mapeamento de tabelas |
| PostgreSQL | Banco de dados relacional |
| Pydantic | Validação de dados |
| Uvicorn | Servidor ASGI |

---

## 📌 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| POST | `/users/` | Criar usuário |
| POST | `/categories/{user_id}` | Criar categoria |
| GET | `/categories/{user_id}` | Listar categorias |
| POST | `/transactions/{user_id}` | Criar transação |
| GET | `/transactions/{user_id}` | Listar transações |
| POST | `/goals/{user_id}` | Criar meta |
| GET | `/goals/{user_id}` | Listar metas |
| GET | `/summary/{user_id}` | Resumo financeiro |

---

## 🚀 Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/vyctorrodrigues/finance-api
cd finance-api
```

**2. Crie o ambiente virtual e instale as dependências**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**3. Configure o banco de dados**

Crie um banco PostgreSQL chamado `finance_db` e configure a `DATABASE_URL` no `database.py`:
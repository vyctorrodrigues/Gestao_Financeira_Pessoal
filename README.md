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
| Passlib & Bcrypt | Criptografia segura de senhas |
| Python-dotenv | Gerenciamento de variáveis de ambiente |
### 🔒 Segurança Aplicada
* **Proteção de Senhas:** Nenhuma credencial de acesso é armazenada em texto limpo. A API utiliza a técnica de hashing com o algoritmo **Bcrypt** para blindar as senhas no banco de dados.
* **Isolamento de Credenciais:** Strings de conexão e senhas do banco PostgreSQL ficam totalmente ocultas em um arquivo `.env` local, respeitando as regras do arquivo `.gitignore`.

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

## 📌 Como configurar o Banco de Dados

Esta API utiliza variáveis de ambiente para proteger as credenciais de acesso ao banco de dados.

1. Na raiz do projeto, duplique o arquivo `.env.example` e renomeie a cópia apenas para `.env`.
2. Abra o novo arquivo `.env` e substitua os valores fictícios pelos dados do seu PostgreSQL local:
   ```text
   DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/finance_db
   ```
3. Certifique-se de ter criado um banco de dados vazio chamado `finance_db` no seu PostgreSQL antes de iniciar o servidor.

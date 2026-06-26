from fastapi import FastAPI
from database import engine, Base
import models.user
import models.category
import models.transaction
import models.goal
from routes import user, category, transaction, goal, summary

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(category.router)
app.include_router(transaction.router)
app.include_router(goal.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Finance API rodando!"}
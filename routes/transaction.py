from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.transaction import Transaction
from schemas.transaction import TransactionCreate, TransactionResponse
import uuid


router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/{user_id}", response_model=TransactionResponse)
def create_transaction(user_id: uuid.UUID, transaction: TransactionCreate, db: Session = Depends(get_db)):
    new_transaction = Transaction(
        id=uuid.uuid4(),
        user_id=user_id,
        category_id=transaction.category_id,
        amount=transaction.amount,
        type=transaction.type,
        date=transaction.date
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@router.get("/{user_id}", response_model=list[TransactionResponse])
def get_transactions(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()
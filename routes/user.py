from opcode import hasjabs

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
import uuid
import hashlib


router = APIRouter(prefix="/users", tags=["user"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    hashed = hashlib.sha256(user.password.encode()).hexdigest()

    new_user = User(
        id=uuid.uuid4(),
        name=user.name,
        email=user.email,
        hashed_password= hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
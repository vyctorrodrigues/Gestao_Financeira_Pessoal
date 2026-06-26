
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
import uuid
from security import gerar_hash_senha


router = APIRouter(prefix="/users", tags=["user"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    senha_criptografada = gerar_hash_senha(user.password)

    new_user = User(
        id=uuid.uuid4(),
        name=user.name,
        email=user.email,
        hashed_password=senha_criptografada
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
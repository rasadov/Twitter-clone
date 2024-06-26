from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..utils import hash_password
from ..db import get_db
from ..models import User
from ..excetions import Exception404
from ..schemas import *

router = APIRouter(
    prefix='/users',
    tags=["Users"]
)

@router.post("/create", status_code=201, response_model=MessageSchema)
def create_user(userSchema: UserSchema, db: Session = Depends(get_db)):
    if (db.query(User).filter(User.email == userSchema.email).first() != None):
        return {
            "message": "user already exists!"
        }
    userSchema.password = hash_password(userSchema.password)
    new_user = User(userSchema.email, userSchema.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "successfully added your request!",
        "data": {
                "email": new_user.email,
                "created_at": new_user.created_at
            }
        }

@router.get("/{id}", response_model=UserOutSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise Exception404
    
    return user

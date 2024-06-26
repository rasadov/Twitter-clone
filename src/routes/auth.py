from fastapi import Depends, APIRouter, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas import Token
from ..models import User
from ..utils import verify_password
from . import oauth2

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login', response_model=Token)
def login(cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == cred.username).first()
    if user == None or not verify_password(cred.password, user.password_hash):
        raise HTTPException(status_code=403, detail="Invalid credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

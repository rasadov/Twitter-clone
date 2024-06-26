from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserOutSchema(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostSchema(BaseModel):
    primary_key: Optional[int] = None
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    owner: UserOutSchema

class UserSchema(BaseModel):
    email: EmailStr
    password: str

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class MessageSchema(BaseModel):
    message: str
    data: Optional[object] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class LikeSchema(BaseModel):
    post_id: int

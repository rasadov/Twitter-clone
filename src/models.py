from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


from .db import Base

class Post(Base):
    __tablename__ = "Posts"
    primary_key = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("UserModel.id",
                                         ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=False)
    rating = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text("now()"))
    owner = relationship("User")

    def __init__(self, data, user_id):
        self.user_id = user_id
        self.title = data.get("title")
        self.content = data.get("content")
        self.published = data.get("published")
        self.rating = data.get("rating")

    def update(self, data, user_id):
        self.user_id = user_id
        self.title = data.get("title")
        self.content = data.get("content")
        self.published = data.get("published")
        self.rating = data.get("rating") if data.get("rating") != None else self.rating

class User(Base):
    __tablename__= "UserModel"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    phone_number = Column(String, nullable=True)

    @property
    def password(self) -> str:
        return self.password
    
    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = password

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Like(Base):
    __tablename__ = "Likes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("UserModel.id", ondelete="CASCADE"))
    post_id = Column(Integer, ForeignKey("Posts.primary_key", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

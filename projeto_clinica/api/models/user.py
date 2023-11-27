from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from data.config import Base
from person import Person

class User(Base):
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True, index=True)
    persons_id = Column(Integer, ForeignKey('Persons.id'))
    username: str = Column(String(40), nullable=False)
    password: str = Column(String(8), nullable=False)

class UserBase(BaseModel):
    username: str
    password: str

class UserRequest(UserBase):
    ...

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True

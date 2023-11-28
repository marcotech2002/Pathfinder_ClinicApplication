from sqlalchemy import Column, Integer, String, ForeignKey
from data.data_base_config import Base
from sqlalchemy.orm import relationship, Mapped
from person import Person
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class User(Base):
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True, index=True)
    persons_id = Column(Integer, ForeignKey('Persons.id'))
    username: str = Column(String(40), nullable=False)
    password: str = Column(String(8), nullable=False)

    person: Mapped["Person"] = relationship("Person")

class UserBase(BaseModel):
    username: str
    password: str
    person: Person

class UserRequest(UserBase):
    ...

class UserResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

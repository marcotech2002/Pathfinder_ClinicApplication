from sqlalchemy import Column, Integer, String
from data.data_base_config import Base
from sqlalchemy.orm import relationship, Mapped
from phone import Phone
from typing import List, Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class Person(Base):
    __tablename__ = "Persons"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(30), nullable=False)
    cep = Column(String(8), nullable=False)
    state = Column(String(2), nullable=False)
    city = Column(String(45), nullable=False)
    neighborhood = Column(String(20), nullable=False)
    street = Column(String(45), nullable=False)

    phones: Mapped[List["Phone"]] = relationship("Phone")

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    cep: str
    state: str
    city: str
    neighborhood: str
    street: str
    phones: list[Phone] = []

class PersonRequest(PersonBase):
    ...

class PersonResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

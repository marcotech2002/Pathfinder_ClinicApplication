from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from data.config import Base

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
    

class PersonBase(BaseModel):
    

class PersonRequest(PersonBase):
    ...

class PersonResponse(PersonBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True

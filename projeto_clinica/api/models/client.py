from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from data.config import Base
from person import Person

class Client(Base):
    __tablename__ = "Clients"

    id: int = Column(Integer, primary_key=True, index=True)
    persons_id = Column(Integer, ForeignKey('Persons.id'))

class ClientBase(BaseModel):
    persons_id: int

class ClientRequest(ClientBase):
    ...

class ClientResponse(ClientBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True

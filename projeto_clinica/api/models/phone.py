from sqlalchemy import Column, Integer, String, ForeignKey
from data.data_base_config import Base
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class Phone(Base):
    __tablename__ = "Phones"

    id: int = Column(Integer, primary_key=True, index=True)
    persons_id: int = Column(Integer, ForeignKey('Persons.id'))
    phone: str = Column(String(11), nullable=False)

class PhoneBase(BaseModel):
    persons_id: int
    phone: str

class PhoneRequest(PhoneBase):
    ...

class PhoneResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

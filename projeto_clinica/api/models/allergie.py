from typing import List, Generic, TypeVar, Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel
from pydantic.generics import GenericModel
from data.data_base_config import Base
from sqlalchemy.orm import relationship, Mapped
from models.allergie_type import AllergieType

T = TypeVar('T')

class Allergie(Base):
    __tablename__ = "Allergies"

    id: int = Column(Integer, primary_key=True, index=True)
    allergies_types_id: int = Column(Integer, ForeignKey('Allergies_types.id'))
    name: str = Column(String(20), nullable=False)
    nivel: int = Column(String(8), nullable=False)

    allergie_type: relationship("AllergieType")

class AllergieBase(BaseModel):
    allergies_types_id: int
    name: str
    nivel: int
    allergie_type: AllergieType

class AllergieRequest(AllergieBase):
    ...

class AllergieResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

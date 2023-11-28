from typing import List, Generic, TypeVar, Optional
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from pydantic.generics import GenericModel
from data.data_base_config import Base

T = TypeVar('T')

class AllergieType(Base):
    __tablename__ = "Allergies_types"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(25), nullable=False)

class AllergieTypeBase(BaseModel):
    name: str

class AllergieTypeRequest(AllergieTypeBase):
    ...

class AllergieTypeResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
from sqlalchemy import Column, Integer, String
from data.data_base_config import Base
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class MedicineType(Base):
    __tablename__ = "Medicines_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)

class MedicineTypeBase(BaseModel):
    name: str

class MedicineTypeRequest(MedicineTypeBase):
    ...

class MedicineTypeResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

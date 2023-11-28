from sqlalchemy import Column, Integer, String, ForeignKey
from data.data_base_config import Base
from sqlalchemy.orm import relationship, Mapped
from medicine_type import MedicineType
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class Medicine(Base):
    __tablename__ = "Medicines"

    id = Column(Integer, primary_key=True, index=True)
    medicines_types_id = Column(Integer, ForeignKey('Clients.persons_id')),
    name = Column(String(20), nullable=False),

    medicine_type: Mapped["MedicineType"] = relationship("MedicineType")

class MedicineBase(BaseModel):
    medicines_types_id: int
    name: str
    medicine_type: MedicineType

class MedicineRequest(MedicineBase):
    ...

class MedicineResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

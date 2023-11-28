from sqlalchemy import Column, Integer, String, ForeignKey
from data.data_base_config import Base
from sqlalchemy.orm import relationship, Mapped
from disease_type import DiseaseType
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class Disease(Base):
    __tablename__ = "Diseases"

    id = Column(Integer, primary_key=True, index=True)
    diseases_types_id = Column(Integer, ForeignKey('Diseases_types.id')),
    name = Column(String(40), nullable=False),

    disease_type: Mapped["DiseaseType"] = relationship("DiseaseType")

class DiseaseBase(BaseModel):
    diseases_types_id: int
    name: str
    disease_type: DiseaseType

class DiseaseRequest(DiseaseBase):
    ...

class DiseaseResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

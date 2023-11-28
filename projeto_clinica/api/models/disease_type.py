from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from data.data_base_config import Base
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class DiseaseType(Base):
    __tablename__ = "Diseases_types"

    id = Column(Integer, primary_key=True, index=True),
    name = Column(String(25), nullable=False)

class DiseaseTypeBase(BaseModel):
    name: str

class DiseaseTypeRequest(DiseaseTypeBase):
    ...

class DiseaseTypeResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
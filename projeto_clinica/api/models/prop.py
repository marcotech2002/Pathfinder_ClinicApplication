from sqlalchemy import Column, Integer, String
from data.data_base_config import Base
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class Prop(Base):
    __tablename__ = "Props"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), nullable=False)

class PropBase(BaseModel):
    name: str

class PropRequest(PropBase):
    ...

class PropResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

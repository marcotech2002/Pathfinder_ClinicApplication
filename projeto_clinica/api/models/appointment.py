from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from data.data_base_config import Base
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

class Appointment(Base):
    __tablename__ = "Appointments"

    id = Column(Integer, primary_key=True, index=True)
    persons_id = Column(Integer, ForeignKey('Persons.id'))
    schedule = Column(DateTime, nullable=False)
    note = Column(String(255), nullable=False)

class AppointmentBase(BaseModel):
    persons_id: int
    schedule: datetime
    note: str

class AppointmentRequest(AppointmentBase):
    ...

class AppointmentResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

from sqlalchemy import Column, Integer, ForeignKey, Table
from data.data_base_config import Base
from sqlalchemy.orm import relationship, Mapped
from person import Person
from appointment import Appointment
from medicine import Medicine
from prop import Prop
from allergie import Allergie
from disease import Disease
from typing import List, Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T')

Medicines_Clients = Table(
    "Medicines_Clients",
    Base.metadata,
    Column("persons_id", Integer, ForeignKey('Clients.persons_id'), primary_key=True),
    Column("medicines_id", Integer, ForeignKey('Medicines.id'), primary_key=True)
)

Clients_Props = Table(
    "Clients_Props",
    Base.metadata,
    Column("persons_id", Integer, ForeignKey('Clients.persons_id'), primary_key=True),
    Column("props_id", Integer, ForeignKey('Props.id'), primary_key=True),
    Column("dose", Integer, nullable=False)
)

Allergies_Clients = Table(
    "Allergies_Clients",
    Base.metadata,
    Column("persons_id", Integer, ForeignKey('Clients.persons_id'), primary_key=True),
    Column("allergies_id", Integer, ForeignKey('Allergies.id'), primary_key=True)
)

Diseases_Clients = Table(
    "Diseases_Clients",
    Base.metadata,
    Column("persons_id", Integer, ForeignKey('Clients.persons_id'), primary_key=True),
    Column("diseases_id", Integer, ForeignKey('diseases.id'), primary_key=True)
)

class Client(Base):
    __tablename__ = "Clients"

    id = Column(Integer, primary_key=True, index=True)
    persons_id = Column(Integer, ForeignKey('Persons.id'))

    person: Person = relationship(Person)
    appointments: Mapped[List["Appointment"]] = relationship("Appointment")
    medicines: Mapped[List["Medicine"]] = relationship("Medicine", secondary=Medicines_Clients)
    props: Mapped[List["Prop"]] = relationship("Prop", secondary=Clients_Props)
    allergies: Mapped[List["Allergie"]] = relationship("Allergie", secondary=Allergies_Clients)
    diseases: Mapped[List["Disease"]] = relationship("Disease", secondary=Diseases_Clients)

class ClientBase(BaseModel):
    persons_id: int
    person: Person
    appointments: List[Appointment] = []
    medicines: List[Medicine] = []
    props: List[Prop] = []
    allergies: List[Allergie] = []
    diseases: List[Disease] = []

class ClientRequest(ClientBase):
    ...

class ClientResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

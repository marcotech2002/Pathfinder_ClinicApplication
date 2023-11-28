from __future__ import annotations
from sqlalchemy.orm import Session
from models.appointment import Appointment

class AppointmentRepository:
    @staticmethod
    def get_all(db:Session) -> list[Appointment]:
        return db.query(Appointment).all()

    @staticmethod
    def create(db: Session, Appointment: Appointment) -> Appointment:
        if Appointment.id:
            db.merge(Appointment)
        else:
            db.add(Appointment)
        db.commit()
        return Appointment

    @staticmethod
    def get_by_id(db: Session, id: int) -> Appointment:
        return db.query(Appointment).filter(Appointment.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _appointment = AppointmentRepository.get_by_id(db, id)
        if _appointment is not None:
            db.delete(_appointment)
            db.commit()
    
    @staticmethod
    def update(db: Session, Appointment: Appointment) -> Appointment:
        _appointment = AppointmentRepository.get_by_id(db, Appointment.id)
        _appointment = Appointment
        db.commit()
        return _appointment
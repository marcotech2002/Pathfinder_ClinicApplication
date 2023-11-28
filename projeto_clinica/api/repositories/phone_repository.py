from __future__ import annotations
from sqlalchemy.orm import Session
from models.phone import Phone

class PhoneRepository:
    @staticmethod
    def get_all(db:Session) -> list[Phone]:
        return db.query(Phone).all()

    @staticmethod
    def create(db: Session, Phone: Phone) -> Phone:
        if Phone.id:
            db.merge(Phone)
        else:
            db.add(Phone)
        db.commit()
        return Phone

    @staticmethod
    def get_by_id(db: Session, id: int) -> Phone:
        return db.query(Phone).filter(Phone.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _phone = PhoneRepository.get_by_id(db, id)
        if _phone is not None:
            db.delete(_phone)
            db.commit()
    
    @staticmethod
    def update(db: Session, Phone: Phone) -> Phone:
        _phone = PhoneRepository.get_by_id(db, Phone.id)
        _phone = Phone
        db.commit()
        return _phone
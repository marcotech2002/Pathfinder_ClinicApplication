from __future__ import annotations
from sqlalchemy.orm import Session
from models.medicine import Medicine

class MedicineRepository:
    @staticmethod
    def get_all(db:Session) -> list[Medicine]:
        return db.query(Medicine).all()

    @staticmethod
    def create(db: Session, Medicine: Medicine) -> Medicine:
        if Medicine.id:
            db.merge(Medicine)
        else:
            db.add(Medicine)
        db.commit()
        return Medicine

    @staticmethod
    def get_by_id(db: Session, id: int) -> Medicine:
        return db.query(Medicine).filter(Medicine.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _medicine = MedicineRepository.get_by_id(db, id)
        if _medicine is not None:
            db.delete(_medicine)
            db.commit()
    
    @staticmethod
    def update(db: Session, Medicine: Medicine) -> Medicine:
        _medicine = MedicineRepository.get_by_id(db, Medicine.id)
        _medicine = Medicine
        db.commit()
        return _medicine
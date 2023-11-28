from __future__ import annotations
from sqlalchemy.orm import Session
from models.medicine_type import MedicineType

class MedicineTypeRepository:
    @staticmethod
    def get_all(db:Session) -> list[MedicineType]:
        return db.query(MedicineType).all()

    @staticmethod
    def create(db: Session, MedicineType: MedicineType) -> MedicineType:
        if MedicineType.id:
            db.merge(MedicineType)
        else:
            db.add(MedicineType)
        db.commit()
        return MedicineType

    @staticmethod
    def get_by_id(db: Session, id: int) -> MedicineType:
        return db.query(MedicineType).filter(MedicineType.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _medicineType = MedicineTypeRepository.get_by_id(db, id)
        if _medicineType is not None:
            db.delete(_medicineType)
            db.commit()
    
    @staticmethod
    def update(db: Session, MedicineType: MedicineType) -> MedicineType:
        _medicineType = MedicineTypeRepository.get_by_id(db, MedicineType.id)
        _medicineType = MedicineType
        db.commit()
        return _medicineType
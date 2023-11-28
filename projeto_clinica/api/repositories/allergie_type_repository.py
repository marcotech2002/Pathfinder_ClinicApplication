from __future__ import annotations
from sqlalchemy.orm import Session
from models.allergie_type import AllergieType

class AllergieTypeRepository:
    @staticmethod
    def get_all(db:Session) -> list[AllergieType]:
        return db.query(AllergieType).all()

    @staticmethod
    def create(db: Session, AllergieType: AllergieType) -> AllergieType:
        if AllergieType.id:
            db.merge(AllergieType)
        else:
            db.add(AllergieType)
        db.commit()
        return AllergieType

    @staticmethod
    def get_by_id(db: Session, id: int) -> AllergieType:
        return db.query(AllergieType).filter(AllergieType.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _allergieType = AllergieTypeRepository.get_by_id(db, id)
        if _allergieType is not None:
            db.delete(_allergieType)
            db.commit()
    
    @staticmethod
    def update(db: Session, AllergieType: AllergieType) -> AllergieType:
        _allergieType = AllergieTypeRepository.get_by_id(db, AllergieType.id)
        _allergieType = AllergieType
        db.commit()
        return _allergieType
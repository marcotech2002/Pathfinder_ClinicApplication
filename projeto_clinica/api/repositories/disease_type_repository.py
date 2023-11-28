from __future__ import annotations
from sqlalchemy.orm import Session
from models.disease_type import DiseaseType

class DiseaseTypeRepository:
    @staticmethod
    def get_all(db:Session) -> list[DiseaseType]:
        return db.query(DiseaseType).all()

    @staticmethod
    def create(db: Session, DiseaseType: DiseaseType) -> DiseaseType:
        if DiseaseType.id:
            db.merge(DiseaseType)
        else:
            db.add(DiseaseType)
        db.commit()
        return DiseaseType

    @staticmethod
    def get_by_id(db: Session, id: int) -> DiseaseType:
        return db.query(DiseaseType).filter(DiseaseType.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _diseaseType = DiseaseTypeRepository.get_by_id(db, id)
        if _diseaseType is not None:
            db.delete(_diseaseType)
            db.commit()
    
    @staticmethod
    def update(db: Session, DiseaseType: DiseaseType) -> DiseaseType:
        _diseaseType = DiseaseTypeRepository.get_by_id(db, DiseaseType.id)
        _diseaseType = DiseaseType
        db.commit()
        return _diseaseType
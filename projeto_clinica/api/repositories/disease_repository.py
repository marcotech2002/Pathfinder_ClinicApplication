from __future__ import annotations
from sqlalchemy.orm import Session
from models.disease import Disease

class DiseaseRepository:
    @staticmethod
    def get_all(db:Session) -> list[Disease]:
        return db.query(Disease).all()

    @staticmethod
    def create(db: Session, Disease: Disease) -> Disease:
        if Disease.id:
            db.merge(Disease)
        else:
            db.add(Disease)
        db.commit()
        return Disease

    @staticmethod
    def get_by_id(db: Session, id: int) -> Disease:
        return db.query(Disease).filter(Disease.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _disease = DiseaseRepository.get_by_id(db, id)
        if _disease is not None:
            db.delete(_disease)
            db.commit()
    
    @staticmethod
    def update(db: Session, Disease: Disease) -> Disease:
        _disease = DiseaseRepository.get_by_id(db, Disease.id)
        _disease = Disease
        db.commit()
        return _disease
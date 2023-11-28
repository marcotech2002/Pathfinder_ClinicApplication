from __future__ import annotations
from sqlalchemy.orm import Session
from models.allergie import Allergie

class AllergieRepository:
    @staticmethod
    def get_all(db:Session) -> list[Allergie]:
        return db.query(Allergie).all()

    @staticmethod
    def create(db: Session, Allergie: Allergie) -> Allergie:
        if Allergie.id:
            db.merge(Allergie)
        else:
            db.add(Allergie)
        db.commit()
        return Allergie

    @staticmethod
    def get_by_id(db: Session, id: int) -> Allergie:
        return db.query(Allergie).filter(Allergie.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _allergie = AllergieRepository.get_by_id(db, id)
        if _allergie is not None:
            db.delete(_allergie)
            db.commit()
    
    @staticmethod
    def update(db: Session, Allergie: Allergie) -> Allergie:
        _allergie = AllergieRepository.get_by_id(db, Allergie.id)
        _allergie = Allergie
        db.commit()
        return _allergie
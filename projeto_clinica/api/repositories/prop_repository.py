from __future__ import annotations
from sqlalchemy.orm import Session
from models.prop import Prop

class PropRepository:
    @staticmethod
    def get_all(db:Session) -> list[Prop]:
        return db.query(Prop).all()

    @staticmethod
    def create(db: Session, Prop: Prop) -> Prop:
        if Prop.id:
            db.merge(Prop)
        else:
            db.add(Prop)
        db.commit()
        return Prop

    @staticmethod
    def get_by_id(db: Session, id: int) -> Prop:
        return db.query(Prop).filter(Prop.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _prop = PropRepository.get_by_id(db, id)
        if _prop is not None:
            db.delete(_prop)
            db.commit()
    
    @staticmethod
    def update(db: Session, Prop: Prop) -> Prop:
        _prop = PropRepository.get_by_id(db, Prop.id)
        _prop = Prop
        db.commit()
        return _prop
from __future__ import annotations
from sqlalchemy.orm import Session
from models.person import Person

class PersonRepository:
    @staticmethod
    def get_all(db:Session) -> list[Person]:
        return db.query(Person).all()

    @staticmethod
    def create(db: Session, Person: Person) -> Person:
        if Person.id:
            db.merge(Person)
        else:
            db.add(Person)
        db.commit()
        return Person

    @staticmethod
    def get_by_id(db: Session, id: int) -> Person:
        return db.query(Person).filter(Person.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _person = PersonRepository.get_by_id(db, id)
        if _person is not None:
            db.delete(_person)
            db.commit()
    
    @staticmethod
    def update(db: Session, Person: Person) -> Person:
        _person = PersonRepository.get_by_id(db, Person.id)
        _person = Person
        db.commit()
        return _person
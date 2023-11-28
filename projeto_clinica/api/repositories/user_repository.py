from __future__ import annotations
from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    @staticmethod
    def get_all(db:Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def create(db: Session, User: User) -> User:
        if User.id:
            db.merge(User)
        else:
            db.add(User)
        db.commit()
        return User

    @staticmethod
    def get_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _user = UserRepository.get_by_id(db, id)
        if _user is not None:
            db.delete(_user)
            db.commit()
    
    @staticmethod
    def update(db: Session, User: User) -> User:
        _user = UserRepository.get_by_id(db, User.id)
        _user = User
        db.commit()
        return _user
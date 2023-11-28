from __future__ import annotations
from sqlalchemy.orm import Session
from models.Client import Client

class ClientRepository:
    @staticmethod
    def get_all(db:Session) -> list[Client]:
        return db.query(Client).all()

    @staticmethod
    def create(db: Session, Client: Client) -> Client:
        if Client.id:
            db.merge(Client)
        else:
            db.add(Client)
        db.commit()
        return Client

    @staticmethod
    def get_by_id(db: Session, id: int) -> Client:
        return db.query(Client).filter(Client.id == id).first()

    @staticmethod
    def delete(db: Session, id: int) -> None:
        _client = ClientRepository.get_by_id(db, id)
        if _client is not None:
            db.delete(_client)
            db.commit()
    
    @staticmethod
    def update(db: Session, Client: Client) -> Client:
        _client = ClientRepository.get_by_id(db, Client.id)
        _client = Client
        db.commit()
        return _client
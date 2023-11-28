from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.client_repository import ClientRepository
from models.client import ClientRequest

client_router = APIRouter()

@client_router.get("/api/client")
async def get_all(db: Session = Depends(get_db)):
    _clients = ClientRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_clients).dict(exclude_none=True)

@client_router.post("/api/client")
async def create(request: ClientRequest, db: Session = Depends(get_db)):
    _client = ClientRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_client).dict(exclude_none=True)

@client_router.get("/api/client/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _client = ClientRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_client).dict(exclude_none=True)

@client_router.put("/api/client")
async def get_by_id(request: ClientRequest, db: Session = Depends(get_db)):
    _client = ClientRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_client).dict(exclude_none=True)

@client_router.delete("/api/client/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    ClientRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

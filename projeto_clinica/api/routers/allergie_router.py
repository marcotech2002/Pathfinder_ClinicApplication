from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.allergie_repository import AllergieRepository
from models.allergie import AllergieRequest

allergie_router = APIRouter()

@allergie_router.get("/api/allergie")
async def get_all(db: Session = Depends(get_db)):
    _allergies = AllergieRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_allergies).dict(exclude_none=True)

@allergie_router.post("/api/allergie")
async def create(request: AllergieRequest, db: Session = Depends(get_db)):
    _allergie = AllergieRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_allergie).dict(exclude_none=True)

@allergie_router.get("/api/allergie/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _allergie = AllergieRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_allergie).dict(exclude_none=True)

@allergie_router.put("/api/allergie")
async def get_by_id(request: AllergieRequest, db: Session = Depends(get_db)):
    _allergie = AllergieRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_allergie).dict(exclude_none=True)

@allergie_router.delete("/api/allergie/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    AllergieRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

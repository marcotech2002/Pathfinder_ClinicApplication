from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.allergie_type_repository import AllergieTypeRepository
from models.allergie_type import AllergieTypeRequest

allergie_type_router = APIRouter()

@allergie_type_router.get("/api/allergie_type")
async def get_all(db: Session = Depends(get_db)):
    _allergieTypes = AllergieTypeRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_allergieTypes).dict(exclude_none=True)

@allergie_type_router.post("/api/allergie_type")
async def create(request: AllergieTypeRequest, db: Session = Depends(get_db)):
    _allergieType = AllergieTypeRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_allergieType).dict(exclude_none=True)

@allergie_type_router.get("/api/allergie_type/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _allergieType = AllergieTypeRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_allergieType).dict(exclude_none=True)

@allergie_type_router.put("/api/allergie_type")
async def get_by_id(request: AllergieTypeRequest, db: Session = Depends(get_db)):
    _allergieType = AllergieTypeRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_allergieType).dict(exclude_none=True)

@allergie_type_router.delete("/api/allergie_type/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    AllergieTypeRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

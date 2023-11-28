from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.disease_type_repository import DiseaseTypeRepository
from models.disease_type import DiseaseTypeRequest

disease_type_router = APIRouter()

@disease_type_router.get("/api/disease_type")
async def get_all(db: Session = Depends(get_db)):
    _disease_types = DiseaseTypeRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_disease_types).dict(exclude_none=True)

@disease_type_router.post("/api/disease_type")
async def create(request: DiseaseTypeRequest, db: Session = Depends(get_db)):
    _disease_type = DiseaseTypeRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_disease_type).dict(exclude_none=True)

@disease_type_router.get("/api/disease_type/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _disease_type = DiseaseTypeRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_disease_type).dict(exclude_none=True)

@disease_type_router.put("/api/disease_type")
async def get_by_id(request: DiseaseTypeRequest, db: Session = Depends(get_db)):
    _disease_type = DiseaseTypeRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_disease_type).dict(exclude_none=True)

@disease_type_router.delete("/api/disease_type/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    DiseaseTypeRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

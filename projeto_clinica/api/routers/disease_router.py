from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.disease_repository import DiseaseRepository
from models.disease import DiseaseRequest

disease_router = APIRouter()

@disease_router.get("/api/disease")
async def get_all(db: Session = Depends(get_db)):
    _diseases = DiseaseRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_diseases).dict(exclude_none=True)

@disease_router.post("/api/disease")
async def create(request: DiseaseRequest, db: Session = Depends(get_db)):
    _disease = DiseaseRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_disease).dict(exclude_none=True)

@disease_router.get("/api/disease/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _disease = DiseaseRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_disease).dict(exclude_none=True)

@disease_router.put("/api/disease")
async def get_by_id(request: DiseaseRequest, db: Session = Depends(get_db)):
    _disease = DiseaseRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_disease).dict(exclude_none=True)

@disease_router.delete("/api/disease/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    DiseaseRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

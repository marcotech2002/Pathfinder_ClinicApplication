from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.medicine_repository import MedicineRepository
from models.medicine import MedicineRequest

medicine_router = APIRouter()

@medicine_router.get("/api/medicine")
async def get_all(db: Session = Depends(get_db)):
    _medicines = MedicineRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_medicines).dict(exclude_none=True)

@medicine_router.post("/api/medicine")
async def create(request: MedicineRequest, db: Session = Depends(get_db)):
    _medicine = MedicineRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_medicine).dict(exclude_none=True)

@medicine_router.get("/api/medicine/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _medicine = MedicineRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_medicine).dict(exclude_none=True)

@medicine_router.put("/api/medicine")
async def get_by_id(request: MedicineRequest, db: Session = Depends(get_db)):
    _medicine = MedicineRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_medicine).dict(exclude_none=True)

@medicine_router.delete("/api/medicine/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    MedicineRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

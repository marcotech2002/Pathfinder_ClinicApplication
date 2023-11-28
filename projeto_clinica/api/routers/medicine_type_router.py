from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.medicine_type_repository import MedicineTypeRepository
from models.medicine_type import MedicineTypeRequest

medicine_type_router = APIRouter()

@medicine_type_router.get("/api/medicine_type")
async def get_all(db: Session = Depends(get_db)):
    _medicine_types = MedicineTypeRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_medicine_types).dict(exclude_none=True)

@medicine_type_router.post("/api/medicine_type")
async def create(request: MedicineTypeRequest, db: Session = Depends(get_db)):
    _medicine_type = MedicineTypeRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_medicine_type).dict(exclude_none=True)

@medicine_type_router.get("/api/medicine_type/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _medicine_type = MedicineTypeRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_medicine_type).dict(exclude_none=True)

@medicine_type_router.put("/api/medicine_type")
async def get_by_id(request: MedicineTypeRequest, db: Session = Depends(get_db)):
    _medicine_type = MedicineTypeRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_medicine_type).dict(exclude_none=True)

@medicine_type_router.delete("/api/medicine_type/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    MedicineTypeRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

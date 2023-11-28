from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.appointment_repository import AppointmentRepository
from models.appointment import AppointmentRequest

appointment_router = APIRouter()

@appointment_router.get("/api/appointment")
async def get_all(db: Session = Depends(get_db)):
    _appointments = AppointmentRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_appointments).dict(exclude_none=True)

@appointment_router.post("/api/appointment")
async def create(request: AppointmentRequest, db: Session = Depends(get_db)):
    _appointment = AppointmentRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_appointment).dict(exclude_none=True)

@appointment_router.get("/api/appointment/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _appointment = AppointmentRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_appointment).dict(exclude_none=True)

@appointment_router.put("/api/appointment")
async def get_by_id(request: AppointmentRequest, db: Session = Depends(get_db)):
    _appointment = AppointmentRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_appointment).dict(exclude_none=True)

@appointment_router.delete("/api/appointment/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    AppointmentRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.prop_repository import PropRepository
from models.prop import PropRequest

prop_router = APIRouter()

@prop_router.get("/api/prop")
async def get_all(db: Session = Depends(get_db)):
    _props = PropRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_props).dict(exclude_none=True)

@prop_router.post("/api/prop")
async def create(request: PropRequest, db: Session = Depends(get_db)):
    _prop = PropRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_prop).dict(exclude_none=True)

@prop_router.get("/api/prop/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _prop = PropRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_prop).dict(exclude_none=True)

@prop_router.put("/api/prop")
async def get_by_id(request: PropRequest, db: Session = Depends(get_db)):
    _prop = PropRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_prop).dict(exclude_none=True)

@prop_router.delete("/api/prop/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    PropRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

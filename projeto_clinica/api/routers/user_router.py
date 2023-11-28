from fastapi import APIRouter, Depends, HTTPException, status, Response, Path
from data.data_base_config import SessionLocal, get_db
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from models.user import UserRequest

user_router = APIRouter()

@user_router.get("/api/user")
async def get_all(db: Session = Depends(get_db)):
    _users = UserRepository.get_all(db)
    return Response(code=200, status="OK", message="Tipos de alergia retornados com sucesso!", result=_users).dict(exclude_none=True)

@user_router.post("/api/user")
async def create(request: UserRequest, db: Session = Depends(get_db)):
    _user = UserRepository.create(request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia criado com sucesso!", result=_user).dict(exclude_none=True)

@user_router.get("/api/user/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _user = UserRepository.get_by_id(db, id)
    return Response(code=200, status="OK", message="Tipo de alergia retornado com sucesso!", result=_user).dict(exclude_none=True)

@user_router.put("/api/user")
async def get_by_id(request: UserRequest, db: Session = Depends(get_db)):
    _user = UserRepository.update(db, request.parameter)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!", result=_user).dict(exclude_none=True)

@user_router.delete("/api/user/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    UserRepository.delete(db)
    return Response(code=200, status="OK", message="Tipo de alergia atualizado com sucesso!").dict(exclude_none=True)

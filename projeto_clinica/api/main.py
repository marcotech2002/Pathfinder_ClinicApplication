from typing import Union
from fastapi import FastAPI
from data.data_base_config import engine, Base
from routers.allergie_type_router import allergie_type_router
from routers.allergie_router import allergie_router
from routers.appointment_router import appointment_router
from routers.client_router import client_router
from routers.prop_router import prop_router
from routers.disease_router import disease_router
from routers.user_router import user_router
from routers.medicine_router import medicine_router
from routers.medicine_type_router import medicine_type_router
from routers.disease_type_router import disease_type_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_router)
app.include_router(client_router)
app.include_router(allergie_router)
app.include_router(appointment_router)
app.include_router(disease_router)
app.include_router(medicine_router)
app.include_router(prop_router)
app.include_router(allergie_type_router)
app.include_router(disease_type_router)
app.include_router(medicine_type_router)
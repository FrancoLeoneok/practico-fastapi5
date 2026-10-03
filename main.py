from fastapi import FastAPI
from routers.juegos import router as juegos_router
from routers.estudios import router as estudios_router

app = FastAPI(
    title="API de Juegos y Estudios",
    description="API desarrollada con FastAPI, SQLModel y Alembic",
    version="1.0.0",
)

app.include_router(juegos_router, prefix="/juegos", tags=["Juegos"])
app.include_router(estudios_router, prefix="/estudios", tags=["Estudios"])






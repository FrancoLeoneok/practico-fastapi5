from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_db
from models import (
    Juego,
    JuegoCreate,
    JuegoPublic,
    JuegoPublicNested,
    Estudio,
)

router = APIRouter()


@router.post("/", response_model=JuegoPublic, status_code=201)
def create_juego(juego: JuegoCreate, db: Session = Depends(get_db)):
    if juego.estudio_id is not None:
        estudio = db.get(Estudio, juego.estudio_id)
        if not estudio:
            raise HTTPException(status_code=404, detail="El estudio especificado no existe")
    juego_db = Juego.model_validate(juego)
    db.add(juego_db)
    db.commit()
    db.refresh(juego_db)
    return juego_db


@router.get("/", response_model=List[JuegoPublicNested])
def get_juegos(db: Session = Depends(get_db)):
    juegos = db.exec(select(Juego)).all()
    return juegos


@router.get("/{id}", response_model=JuegoPublicNested)
def get_juego(id: int, db: Session = Depends(get_db)):
    juego = db.get(Juego, id)
    if not juego:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return juego

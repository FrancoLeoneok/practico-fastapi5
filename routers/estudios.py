from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_db
from models import (
    Estudio,
    EstudioCreate,
    EstudioPublic,
    EstudioPublicNested,
)

router = APIRouter()


@router.post("/", response_model=EstudioPublic, status_code=201)
def create_estudio(estudio: EstudioCreate, db: Session = Depends(get_db)):
    estudio_db = Estudio.model_validate(estudio)
    db.add(estudio_db)
    db.commit()
    db.refresh(estudio_db)
    return estudio_db


@router.get("/", response_model=List[EstudioPublic])
def get_estudios(db: Session = Depends(get_db)):
    estudios = db.exec(select(Estudio)).all()
    return estudios


@router.get("/{id}", response_model=EstudioPublicNested)
def get_estudio(id: int, db: Session = Depends(get_db)):
    estudio = db.get(Estudio, id)
    if not estudio:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return estudio

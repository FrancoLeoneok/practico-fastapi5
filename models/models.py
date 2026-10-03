from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class EstudioBase(SQLModel):
    nombre: str = Field(index=True)
    pais: str


class Estudio(EstudioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    juegos: List["Juego"] = Relationship(back_populates="estudio")


class EstudioCreate(EstudioBase):
    pass


class EstudioPublic(EstudioBase):
    id: int


class JuegoBase(SQLModel):
    titulo: str = Field(index=True)
    genero: str
    score: int
    estudio_id: Optional[int] = Field(default=None, foreign_key="estudio.id")


class Juego(JuegoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    estudio: Optional[Estudio] = Relationship(back_populates="juegos")


class JuegoCreate(JuegoBase):
    pass


class JuegoPublic(JuegoBase):
    id: int


# Esquemas para respuestas anidadas
class JuegoPublicNested(JuegoPublic):
    estudio: Optional[EstudioPublic] = None


class EstudioPublicNested(EstudioPublic):
    juegos: List[JuegoPublic] = []
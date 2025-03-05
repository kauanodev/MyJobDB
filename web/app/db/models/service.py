from pydantic import BaseModel


class SelectService(BaseModel):
    id: int
    nome: str
    categoria: str


class InsertService(BaseModel):
    nome: str
    categoria: str

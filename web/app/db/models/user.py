from pydantic import BaseModel


class SelectUser(BaseModel):
    id: int
    nome: str
    cpf: str
    endereco: str
    data_de_nascimento: str


class InsertUser(BaseModel):
    nome: str
    cpf: str
    endereco: str
    data_de_nascimento: str

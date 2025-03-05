from pydantic import BaseModel


class SelectServiceProvider(BaseModel):
    id: int
    nome: str
    cpf: str
    endereco: str
    endereco: str
    data_de_nascimento: str
    additional_info: str


class InsertServiceProvider(BaseModel):
    user_id: int
    additional_info: str

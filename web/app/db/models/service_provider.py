from pydantic import BaseModel


class SelectServiceProvider(BaseModel):
    id: int
    nome: str
    cpf: str
    endereco: str
    endereco: str
    data_de_nascimento: str
    informacoes_adicionais: str


class InsertServiceProvider(BaseModel):
    usuario_id: int
    informacoes_adicionais: str

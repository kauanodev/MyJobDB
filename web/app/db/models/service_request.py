from pydantic import BaseModel


class SelectServiceRequest(BaseModel):
    id: int
    preco: str
    prazo: str
    descricao: str | None
    servico_id: int
    contratante_id: int
    prestador_id: int | None


class InsertServiceRequest(BaseModel):
    preco: str
    prazo: str
    descricao: str | None
    servico_id: int
    contratante_id: int
    prestador_id: int | None

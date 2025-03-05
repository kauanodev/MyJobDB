from pydantic import BaseModel


class SelectServiceContractor(BaseModel):
    usuario_id: int


class InsertServiceContractor(BaseModel):
    usuario_id: int

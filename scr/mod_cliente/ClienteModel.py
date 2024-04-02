from pydantic import BaseModel

class ClienteDB(BaseModel):
    id_cliente: int
    nome: str
    cpf: str
    telefone: str

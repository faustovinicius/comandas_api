from pydantic import BaseModel

class ProdutoDB(BaseModel):
    id_produto: int
    nome: str
    descricao: str
    foto: bytes
    valor_unitario: float

from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    foto: str  # Perguntar pro professor
    valor_unitario: float

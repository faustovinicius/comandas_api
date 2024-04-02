from pydantic import BaseModel

class FuncionarioDB(BaseModel):
    id_funcionario: int
    nome: str
    matricula: str
    cpf: str
    telefone: str
    grupo: int
    senha: str

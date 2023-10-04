from dataclasses import dataclass
import re

@dataclass
class Votacao:
    data_votacao: str
    descricao: str
    link: str
    materia: str
    obs: str
    parlamentar: str
    status_votacao: str
    voto: str

    @classmethod
    def from_dict(cls, values):
        return cls(**values)
    
    def get_id_votacao(url: str):
        id = re.search(pattern= "\d*$", string=url).group(0)
        return id
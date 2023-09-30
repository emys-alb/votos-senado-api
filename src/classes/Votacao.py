from dataclasses import dataclass

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
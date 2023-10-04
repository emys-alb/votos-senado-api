from dataclasses import dataclass

@dataclass
class Senador:
    id_senador: str
    nome: str

    def set_id(self, id: str):
        self.id_senador = id
    
    def set_nome(self, nome: str):
        self.nome = nome
    
    def get_id(self):
        return self.id_senador
    
    def get_nome(self):
        return self.nome
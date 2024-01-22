from dataclasses import dataclass

@dataclass
class Senador:
    id_senador: str
    nome: str
    partido: str

    def set_id(self, id: str):
        self.id_senador = id
    
    def set_nome(self, nome: str):
        self.nome = nome
    
    def set_partido(self, partido: str):
        self.partido = partido
    
    def get_id(self):
        return self.id_senador
    
    def get_nome(self):
        return self.nome
    
    def get_partido(self):
        return self.partido
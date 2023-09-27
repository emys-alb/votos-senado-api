import csv
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


def csv_to_json(csv_file):
      
    #read csv file
    with open(csv_file, encoding='utf-8') as csvf: 
        json_array = []
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        for item in csvReader:
            json_array.append(Votacao.from_dict(dict(item)))
        
        return json_array
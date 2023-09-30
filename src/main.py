from fastapi import FastAPI
from fastapi_pagination import Page, paginate, add_pagination

from datetime import datetime

from src.get_data import csv_to_json
from classes.Votacao import Votacao
from classes.Senador import Senador

data = csv_to_json("data/data.csv")

app = FastAPI()
add_pagination(app)

@app.get("/", response_model=Page[Votacao])
def read_all():
    return paginate(data)

@app.get("/votacao/{data}")
def read_votacoes_por_data(data: str):
    return filter(lambda x: x.data_votacao == data)

@app.get("/votacao/{ano}")
def read_votacoes_por_ano(ano: int):
    filtro = filter(lambda x: datetime.strptime(x.data_votacao, "%d/%m/%Y").year == ano, data)
    return list(filtro)

@app.get("/votos/{id_senador}")
def read_votos_senador(id_senador: str):
    return {"Hello": "World"}

@app.get("/votos/{nome_senador}")
def read_votos_senador(nome_senador: str):
    return {"Hello": "World"}

@app.get("/votos/{id_votacao}/{id_senador}")
def read_votos_senador_votacao(id_votacao: str, id_senador: str):
    return {"Hello": "World"}

@app.get("/votos/{id_votacao}/{nome_senador}")
def read_votos_senador_votacao(id_votacao: str, nome_senador: str):
    return {"Hello": "World"}

@app.get("/votos/{id_votacao}")
def read_votos_por_votacao(id_votacao: str):
    return {"Hello": "World"}
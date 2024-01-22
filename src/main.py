from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi_pagination import Page, paginate, add_pagination

from datetime import datetime

from src.get_data import csv_to_json, get_nome_from_id, get_all_nomes
from src.classes.votacao import Votacao
from src.classes.senador import Senador

data = csv_to_json("data/data.csv")

app = FastAPI()
add_pagination(app)

@app.get("/votacao/", response_model=Page[Votacao])
def read_votacoes_por_data(data_inicio: str, data_fim: Optional[str] = None, formato_data: Optional[str] = None):
    date_format = "%d/%m/%Y" if formato_data is None else formato_data
    
    data_inicio = datetime.strptime(data_inicio, date_format)
    data_fim = datetime.now() if data_fim is None else datetime.strptime(data_fim, date_format)

    filtro = filter(lambda x: data_inicio <= datetime.strptime(x.data_votacao, datetime) <= data_fim, data)
    return paginate(list(filtro))

@app.get("/votos/", response_model=Page[Votacao])
def read_votos_senador(nome_senador: Optional[str] = None, id_senador: Optional[str] = None ):
    if nome_senador is None and id_senador is None:
        return []
    
    if nome_senador is None:
        nome_senador = get_nome_from_id(id_senador)

    filtro = filter(lambda x:  x.parlamentar.strip().lower() == nome_senador, data)
    return paginate(list(filtro))

@app.get("/votos/{id_votacao}/{id_senador}", response_model=Page[Votacao])
def read_votos_senador_votacao(id_votacao: str, id_senador: str, nome_senador: Optional[str] = None):
    filtro_votacao = filter(lambda x: Votacao.get_id_votacao(x.link) == id_votacao, data)
    if nome_senador is None:
        nome_senador = get_nome_from_id(id_senador)
    
    votacoes = list(filtro_votacao)
    filtro = filter(lambda x: x.parlamentar.lower() == nome_senador, votacoes)

    return paginate(list(filtro))

@app.get("/senadores", response_model=Page[Senador])
def read_todos_senadores():
    senadores = get_all_nomes()
    return paginate(list(senadores))

@app.get("/votos/votacao={id_votacao}", response_model=Page[Votacao])
def read_votos_por_votacao(id_votacao: str):
    filtro_votacao = filter(lambda x: Votacao.get_id_votacao(x.link) == id_votacao, data)
    return paginate(list(filtro_votacao))
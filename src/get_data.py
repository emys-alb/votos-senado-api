import csv
import json
import requests

from src.classes.votacao import Votacao


def csv_to_json(csv_file):
    with open(csv_file, encoding='utf-8') as csvf: 
        json_array = []
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        for item in csvReader:
            json_array.append(Votacao.from_dict(dict(item)))
        
        return json_array


def get_lista_senadores():
    url_dados_abertos = "https://legis.senado.leg.br/dadosabertos/arquivos/ListaParlamentarEmExercicio.json?_gl=1*1jg0a97*_ga*MTA0MTgwMDY0OS4xNjc5NTkwMTgx*_ga_CW3ZH25XMK*MTY5NjExMDk2NS4yMS4xLjE2OTYxMTA5NzAuMC4wLjA."
    response = requests.get(url_dados_abertos)
    data = {}
    if response.ok:
        data = json.loads(response.content)

    return data["ListaParlamentarEmExercicio"]["Parlamentares"]["Parlamentar"]


def get_id(nome: str):
    nome = nome.lower()
    senadores = get_lista_senadores()
    id = 0
    for senador in senadores:
        if senador["IdentificacaoParlamentar"]["NomeParlamentar"].strip().lower() == nome or senador["IdentificacaoParlamentar"]["NomeCompletoParlamentar"].strip().lower() == nome:
            return senador["IdentificacaoParlamentar"]["CodigoParlamentar"]
    return id


def get_nome_from_id(id: str):
    senadores = get_lista_senadores()
    for senador in senadores:
        if senador["IdentificacaoParlamentar"]["CodigoParlamentar"] == id:
            return senador["IdentificacaoParlamentar"]["NomeParlamentar"].strip().lower()
    
    return ""

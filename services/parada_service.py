from services.service_sptrans import ServiceSPTRANS
from typing import List
from entidades.parada import Parada
from services.validador_json import ValidadorJson
import pandas as pd
from entidades.posicao import Posicao
import os


class ParadaService(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def buscar_paradas_por_linha(self, id_linha: int) -> List[Parada]:
        path = '/Parada/BuscarParadasPorLinha?codigoLinha=' + str(id_linha)
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            lista_paradas = [Parada(*ValidadorJson(parada).validar_json_parada()) for parada in req]
            return lista_paradas

    def buscar_previsao_chegada_parada_endereco(self, endereco: str):
        path = '/Previsao/Parada?codigoParada=' + endereco
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            return req



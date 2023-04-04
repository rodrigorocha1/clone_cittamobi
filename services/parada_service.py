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

    def buscar_paradas(self, id_linha: int) -> List[Parada]:
        path = '/Parada/BuscarParadasPorLinha?codigoLinha=' + str(id_linha)
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            lista_paradas = [Parada(*ValidadorJson(parada).validar_json_parada()) for parada in req]
            return lista_paradas

    def buscar_todas_posicoes_paradas(self):
        todas_paradas = pd.read_csv(os.getcwd() + '\\data\\raw\\stops.txt')
        paradas = todas_paradas.apply(
            lambda linha: Parada(codigo_parada=linha['stop_id'],
                                 nome_parada=linha['stop_desc'],
                                 endereco_localizacao=linha['stop_name'],
                                 posicao=Posicao(linha['stop_lat'], linha['stop_lon'])), axis=1).tolist()
        return paradas

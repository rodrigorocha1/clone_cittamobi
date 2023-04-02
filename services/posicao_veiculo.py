from typing import List
from entidades.onibus import Onibus
from services.service_sptrans import ServiceSPTRANS


class PosicaoVeiculo(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def buscar_posicoes_veiculos(self, id_linha: int) -> List[Onibus]:
        path = '/Posicao/Linha?codigoLinha=' + str(id_linha)
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            req = req['vs']

            return [Onibus(p) for p in req]

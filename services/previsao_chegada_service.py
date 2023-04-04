from typing import List
from entidades.onibus import Onibus
from entidades.parada import Parada
from services.service_sptrans import ServiceSPTRANS


class PrevisaoChegada(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def buscar_previsao_chegada(self, id_linha: int) -> List[Parada]:
        lista_parada = []
        path = '/Previsao/Linha?codigoLinha=' + str(id_linha)
        if self.__login():
            req = self._sptrans_api.requests_api(path, 'GET')
            for parada in req['ps']:
                p = Parada(parada)
                for onibus in parada['vs']:
                    onibus = Onibus(onibus)
                    p.adicionar_onibus(onibus)
                    lista_parada.append(p)

            return lista_parada

from services.service_sptrans import ServiceSPTRANS
from typing import List
from entidades.parada import Parada


class ParadaService(ServiceSPTRANS):
    def buscar_paradas(self, id_linha: int) -> List[Parada]:
        path = '/Parada/BuscarParadasPorLinha?codigoLinha=' + str(id_linha)
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')
            return [Parada(p) for p in req]

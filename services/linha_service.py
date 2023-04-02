from entidades.linhas import Linha
from services.service_sptrans import ServiceSPTRANS
from typing import List


class LinhaService(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def consultar_linha(self, termo_busca) -> List[Linha]:

        path = '/Linha/Buscar?termosBusca=' + termo_busca
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            return [Linha(linha) for linha in req]
        else:
            pass

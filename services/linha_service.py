from entidades.linhas import Linha
from services.service_sptrans import ServiceSPTRANS
from typing import List
from services.validador_json import ValidadorJson


class LinhaService(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def consultar_linha(self, termo_busca: str) -> List[Linha]:
        """Método para consi

        Args:
            termo_busca (str): Endereço o parte dele EX: USP

        Returns:
            List[Linha]: Uma LIsta de linha
        """
        path = '/Linha/Buscar?termosBusca=' + str(termo_busca)
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            return [Linha(*ValidadorJson(linha).validar_json_linha()) for linha in req]

        else:
            pass

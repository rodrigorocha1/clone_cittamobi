from typing import List
from entidades.onibus import Onibus
from services.service_sptrans import ServiceSPTRANS
from services.validador_json import ValidadorJson


class PosicaoVeiculo(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def buscar_posicoes_veiculos(self, id_linha: int) -> List[Onibus]:
        """Método para buscar a posição do veiculo

        Args:
            id_linha (int): código da linha

        Returns:
            List[Onibus]: lista de ônibus
        """
        path = '/Posicao/Linha?codigoLinha=' + str(id_linha)
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            req = req['vs']
            lista_onibus = [
                Onibus(*ValidadorJson(onibus).validar_json_onibus()) for onibus in req]
            return lista_onibus

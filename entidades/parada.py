from entidades.linhas import Linha
from entidades.posicao import Posicao
from typing import Dict


class Parada:
    def __init__(self, json_parada: Dict):
        self.endereco_localizacao = json_parada['ed'] if json_parada.get('ed') is not None else None
        self.codigo_parada = json_parada['cp'] if json_parada.get('cp') is not None else None
        self.nome_parada = json_parada['np'] if json_parada.get('np') is not None else None
        self._posicao = Posicao(json_parada['py'], json_parada['px'])
        self._linha = []

    @property
    def posicao(self) -> Posicao:
        return self._posicao

    def adicionar_linhas(self, linha: Linha):
        self._onibus.append(linha)

    @property
    def mostrar_onibus(self):
        return self._linha

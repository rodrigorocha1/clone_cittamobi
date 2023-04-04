from entidades.linhas import Linha
from entidades.posicao import Posicao
from typing import Dict


class Parada:
    def __init__(self, endereco_localizacao: str, codigo_parada: int, nome_parada: str, latitude: float, longitude: float):
        self.endereco_localizacao = endereco_localizacao
        self.codigo_parada = codigo_parada
        self.nome_parada = nome_parada
        self._posicao = Posicao(latitude,longitude)
        self._linha = []

    @property
    def posicao(self) -> Posicao:
        return self._posicao

    def adicionar_linhas(self, linha: Linha):
        self._onibus.append(linha)

    @property
    def mostrar_onibus(self):
        return self._linha

from entidades.posicao import Posicao
from entidades.linhas import Linha


class Parada:
    def __init__(self, codigo_parada: int, endereco_localizacao: str, posicao: Posicao):
        self.endereco_localizacao = endereco_localizacao
        self.codigo_parada = codigo_parada
        self._posicao = posicao
        self.__linhas = []

    @property
    def posicao(self):
        return self.posicao

    def adicionar_linha(self, linha: Linha):
        self.__linhas.append(linha)

    def mostrar_linha(self):
        for linha in self.__linhas:
            print(linha)



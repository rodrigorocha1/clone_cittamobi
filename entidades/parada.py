from entidades.posicao import Posicao
from entidades.linhas import Linha
from entidades.posicao import Posicao


class Parada:
    def __init__(self, json_parada):
        self.endereco_localizacao = json_parada['ed']
        self.codigo_parada = json_parada['cp']
        self.nome_parada = json_parada['np']
        self._posicao = Posicao(json_parada['px'], json_parada['py'])
        self.__linhas = []

    @property
    def posicao(self) -> Posicao:
        return self._posicao

    def adicionar_linha(self, linha: Linha):
        self.__linhas.append(linha)

    def mostrar_linha(self):
        for linha in self.__linhas:
            print(linha)

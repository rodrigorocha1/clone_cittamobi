from entidades.posicao import Posicao


class Onibus:
    def __init__(self, acessibiliade: bool, prefixo: str, posicao: Posicao):
        self.acessibiliade = acessibiliade
        self.prefixo = prefixo
        self._posicao = posicao

    @property
    def posicao(self) -> Posicao:
        return self._posicao

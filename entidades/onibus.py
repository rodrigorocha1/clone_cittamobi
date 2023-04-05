from entidades.posicao import Posicao


class Onibus:
    def __init__(self, acessibiliade: bool, prefixo: str, posicao: Posicao, horario_previsto: str=None):
        self.acessibiliade = acessibiliade
        self.horario_previsto = horario_previsto
        self.prefixo = prefixo
        self._posicao = posicao

    @property
    def posicao(self) -> Posicao:
        return self._posicao

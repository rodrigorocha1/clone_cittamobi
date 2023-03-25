from entidades.posicao import Posicao


class Onibus:
    def __init__(self, json):
        self.acessibiliade = json['a']
        self.prefixo = json['p']
        self._posicao = Posicao(json['py'], json['px'])

    @property
    def posicao(self) -> Posicao:
        return self._posicao

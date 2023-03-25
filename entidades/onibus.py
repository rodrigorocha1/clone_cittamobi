from entidades.posicao import Posicao


class Onibus:
    def __init__(self, posicao: Posicao, id_onibus: int, latitude: float = None, acessibiliade=None, longitude=None):
        self.acessibiliade = acessibiliade
        self.id_onibus = id_onibus
        self.latitude = latitude
        self.longitude = longitude
        self._posicao = posicao

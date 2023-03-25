from entidades.posicao import Posicao


class Onibus:
    def __init__(self, id_onibus, latitude, longitude, acessibiliade):
        self.acessibiliade = acessibiliade
        self.id_onibus = id_onibus
        self.latitude = latitude
        self.longitude = longitude
        self.posicao = Posicao()

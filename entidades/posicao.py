class Posicao:
    def __init__(self, latitude: float, longitude: float, horario_captura: float = None):

        self.horario_captura = horario_captura
        self.longitude = longitude
        self.latitude = latitude


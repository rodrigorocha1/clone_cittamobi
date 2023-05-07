class Posicao:
    def __init__(self, latitude: float, longitude: float, horario_captura: float = None):
        """Classe que representa a posição

        Args:
            latitude (float): latitude
            longitude (float): longitude
            horario_captura (float, optional): Horário pevisto. Defaults to None.
        """

        self.horario_captura = horario_captura
        self.longitude = longitude
        self.latitude = latitude

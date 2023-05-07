from entidades.posicao import Posicao


class Onibus:
    def __init__(self, acessibiliade: bool, prefixo: str, posicao: Posicao, horario_previsto: str = None):
        """Classe do ônibus

        Args:
            acessibiliade (bool): Indica se o veículo é (true) ou não (false) acessível para pessoas com deficiência
            prefixo (str): Prefixo do veículo
            posicao (Posicao): Latitude e longitude do veiculo
            horario_previsto (str, optional): horário do chegada na parada. Defaults to None.
        """
        self.acessibiliade = acessibiliade
        self.horario_previsto = horario_previsto
        self.prefixo = prefixo
        self._posicao = posicao

    @property
    def posicao(self) -> Posicao:
        return self._posicao

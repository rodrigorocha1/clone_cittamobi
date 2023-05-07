from entidades.linhas import Linha
from entidades.posicao import Posicao


class Parada:
    def __init__(self, endereco_localizacao: str, codigo_parada: int, nome_parada: str, posicao: Posicao):
        """Classe que representa uma parada

        Args:
            endereco_localizacao (str): Endereço de localização da parada
            codigo_parada (int): Código identificador da parada
            nome_parada (str): Nome da parada
            posicao (Posicao): _Posição
        """
        self.endereco_localizacao = endereco_localizacao
        self.codigo_parada = codigo_parada
        self.nome_parada = nome_parada
        self._posicao = posicao
        self._linha = []

    @property
    def posicao(self) -> Posicao:
        """Método para retornar uma posicão

        Returns:
            Posicao: objeto posição
        """
        return self._posicao

    def adicionar_linhas(self, linha: Linha):
        """Adiciona uma linha na parada

        Args:
            linha (Linha): objeto de linha
        """
        self._linha.append(linha)

    @property
    def mostrar_linha(self):
        """Mostra as linhas que passam na parada 

        Returns:
            _type_: retorna as linhas
        """
        return self._linha

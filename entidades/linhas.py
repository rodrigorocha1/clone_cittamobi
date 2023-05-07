from entidades.onibus import Onibus
import pandas as pd
from entidades.trajeto import Trajeto
import os
from typing import List


class Linha:

    def __init__(self, codigo_identificador: int,
                 modo_circular: bool,
                 letreiro_numerico: str,
                 letreiro_numerico_segunda_parte: str,
                 sentido_linha: int,
                 terminal_principal: str,
                 terminal_secundario: str,
                 quantidade_veiculos=0) -> None:
        """Classe que representa uma lina

        Args:
            codigo_identificador (int):  Código identificador da linha. Este é um código identificador único de cada linha do sistema (por sentido de operação)
            modo_circular (bool): Indica se uma linha opera no modo circular (sem um terminal secundário)
            letreiro_numerico (str):  Informa a primeira parte do letreiro numérico da linha
            letreiro_numerico_segunda_parte (str): Informa a segunda parte do letreiro numérico da linha
            sentido_linha (int):  Informa o sentido ao qual a linha atende, onde 1 significa Terminal Principal para Terminal Secundário e 2 para Terminal Secundário para Terminal Principal
            terminal_principal (str):  Informa o letreiro descritivo da linha no sentido Terminal Principal para Terminal Secundário
            terminal_secundario (str):  Informa o letreiro descritivo da linha no sentido Terminal Secundário para Terminal Principal
            quantidade_veiculos (int, optional): quantidade de veiculos Defaults to 0.
        """

        self.codigo_identificador = codigo_identificador
        self.modo_circular = modo_circular
        self.letreiro_numerico = letreiro_numerico
        self.letreiro_numerico_segunda_parte = letreiro_numerico_segunda_parte
        self.sentido_linha = sentido_linha
        self.terminal_principal = terminal_principal
        self.terminal_secundario = terminal_secundario
        self.quantidade_veiculos = quantidade_veiculos
        self.__onibus = []
        self.trajeto = Trajeto(self.letreiro_numerico + '-' +
                               str(self.letreiro_numerico_segunda_parte))

    def adicionar_onibus(self, onibus: Onibus) -> None:
        """_summary_

        Args:
            onibus (Onibus): Objeto ônibus
        """
        self.__onibus.append(onibus)

    @property
    def onibus(self) -> List[Onibus]:
        """Metódo para adicionar um ônibus da linha

        Returns:
            List[Onibus]: Retorna uma lista de objeto ônibus
        """
        return self.__onibus

    def total_onibus_circulacao(self):
        """Método para retornar os ônibus em operação

        Returns:
            _type_: Total de ônibus
        """
        return len(self.__onibus)

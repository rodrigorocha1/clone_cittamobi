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
        self.__onibus.append(onibus)

    @property
    def onibus(self) -> List[Onibus]:
        return self.__onibus

    def total_onibus_circulacao(self):
        return len(self.__onibus)

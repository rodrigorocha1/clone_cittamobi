from entidades.onibus import Onibus
import pandas as pd
from entidades.trajeto import Trajeto
import os


class Linha:

    @staticmethod
    def listagem_linhas():
        base_linhas = pd.read_csv(os.getcwd() + '\\data\\raw\\routes.txt')
        lista_linhas = base_linhas.apply(
            lambda row: Linha(codigo_identificador=None,
                              sentido_linha=None,
                              modo_circular=None,
                              letreiro_numerico=base_linhas['route_id'].str.split('-')[0],
                              letreiro_numerico_segunda_parte=base_linhas['route_id'].str.split('-')[0],
                              terminal_principal=base_linhas['route_long_name'].str.split('-')[0],
                              terminal_secundario=base_linhas['route_long_name'].str.split('-')[1]), axis=1).tolist()
        return

    def __init__(self, codigo_identificador: int,
                 modo_circular: bool,
                 letreiro_numerico: int,
                 letreiro_numerico_segunda_parte: int,
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
        print(self.letreiro_numerico, self.letreiro_numerico_segunda_parte)
        self.trajeto = Trajeto(self.letreiro_numerico + '-' +
                               str(self.letreiro_numerico_segunda_parte))

    def adicionar_onibus(self, onibus: Onibus) -> None:
        self.__onibus.append(onibus)

    @property
    def onibus(self) -> None:
        return self.__onibus

    def __str__(self):
        return str(self.codigo_identificador) + ' ' \
                                                '' + str(self.modo_circular) + ' ' + str(self.letreiro_numerico) + str(
            self.sentido_linha) + ' ' + \
            self.terminal_principal + ' ' + self.terminal_secundario + ' ' + str(
                self.quantidade_veiculos) + self.cor_trajeto

    def total_onibus_circulacao(self):
        return len(self.__onibus)

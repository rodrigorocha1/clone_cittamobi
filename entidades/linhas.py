from entidades.onibus import Onibus
import pandas as pd
from typing import Dict


class Linha:
    base = pd.read_csv('../data/raw/routes.txt', delimiter=',')

    def __init__(self, json_linha: Dict[str, object], quantidade_veiculos=0) -> None:
        self.codigo_identificador = json_linha['cl'] if json_linha.get('cl') is not None else None
        self.modo_circular = json_linha['lc'] if json_linha.get('lc') is not None else None
        self.letreiro_numerico = json_linha['lt'] if json_linha.get('lt') is not None else None
        self.letreiro_numerico_segunda_parte = json_linha['tl'] if json_linha.get('tl') is not None else None
        self.sentido_linha = json_linha['sl'] if json_linha.get('sl') is not None else None
        self.terminal_principal = json_linha['tp'] if json_linha.get('tp') is not None else None
        self.terminal_secundario = json_linha['ts'] if json_linha.get('ts') is not None else None
        self.quantidade_veiculos = quantidade_veiculos
        self.__onibus = []
        self.cor_trajeto = self.base[self.base['route_id'] == self.letreiro_numerico + '-' +
                                     str(self.letreiro_numerico_segunda_parte)]['route_color'].iloc[0]

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

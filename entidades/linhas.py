from entidades.onibus import Onibus
import pandas as pd


class Linha:
    base = pd.read_csv('../data/raw/routes.txt', delimiter=',')

    def __init__(self, json_linha, quantidade_veiculos=0) -> None:
        self.codigo_identificador = json_linha['cl']
        self.modo_circular = json_linha['lc']
        self.letreiro_numerico = json_linha['lt']
        self.letreiro_numerico_segunda_parte = json_linha['tl']
        self.sentido_linha = json_linha['sl']
        self.terminal_principal = json_linha['tp']
        self.terminal_secundario = json_linha['ts']
        self.quantidade_veiculos = quantidade_veiculos
        self.__onibus = []
        self.cor_trajeto = self.base[self.base['route_id'] == self.letreiro_numerico + '-' +
                                     str(self.letreiro_numerico_segunda_parte)]['route_color'].iloc[0]

    def adicionar_onibus(self, onibus: Onibus) -> None:
        self.__onibus.append(onibus)

    def mostrar_relacao_onibus(self) -> None:
        print('linha', self.codigo_identificador)
        for onibus in self.__onibus:
            print(onibus.id_onibus)

    def __str__(self):
        return str(self.codigo_identificador) + ' ' \
                                                '' + str(self.modo_circular) + ' ' + str(self.letreiro_numerico) + str(
            self.sentido_linha) + ' ' + \
            self.terminal_principal + ' ' + self.terminal_secundario + ' ' + str(
                self.quantidade_veiculos) + self.cor_trajeto

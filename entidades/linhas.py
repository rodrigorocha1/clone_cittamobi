from entidades.onibus import Onibus


class Linha:
    def __init__(self, json_linha, quantidade_veiculos=0) -> None:
        self.codigo_identificador = json_linha['cl']
        self.modo_circular = json_linha['lc']
        self.letreiro_numerico = json_linha['lt']
        self.sentido_linha = json_linha['sl']
        self.terminal_principal = json_linha['tp']
        self.terminal_secundario = json_linha['ts']
        self.quantidade_veiculos = quantidade_veiculos
        self.__onibus = []

    def adicionar_onibus(self, onibus: Onibus) -> None:
        self.__onibus.append(onibus)

    def mostrar_relacao_onibus(self) -> None:
        print('linha', self.codigo_identificador)
        for onibus in self.__onibus:
            print(onibus.id_onibus)

    def __str__(self):
        return str(self.codigo_identificador) + ' ' + str(self.modo_circular) + ' ' + str(self.letreiro_numerico) + str(
            self.sentido_linha) + ' ' + \
            self.terminal_principal + ' ' + self.terminal_secundario + ' ' + str(self.quantidade_veiculos)

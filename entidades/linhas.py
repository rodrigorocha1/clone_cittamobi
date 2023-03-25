from entidades.onibus import Onibus


class Linha:
    def __init__(self, codigo_identificador: int, letreiro_numerico: str, modo_circular: bool, sentido_linha: int,
                 terminal_principal: str, terminal_secundario: str):
        self.codigo_identificador = codigo_identificador
        self.modo_circular = modo_circular
        self.letreiro_numerico = letreiro_numerico
        self.sentido_linha = sentido_linha
        self.terminal_principal = terminal_principal
        self.terminal_secundario = terminal_secundario
        self.__onibus = []

    def adicionar_onibus(self, onibus: Onibus):
        self.__onibus.append(onibus)

    def mostrar_relacao_onibus(self):
        print('linha', self.codigo_identificador)
        for onibus in self.__onibus:
            print(onibus.id_onibus)

from entidades.onibus import Onibus


class Linha:
    def __init__(self, codigo_identificador: int, lt: str, modo_circular: bool, sl: int, tp: str, ts: str):
        self.codigo_identificador = codigo_identificador
        self.modo_circular = modo_circular
        self.lt = lt
        self.sl = sl
        self.tp = tp
        self.ts = ts
        self.__onibus = []

    def adionar_onibus(self, onibus: Onibus):
        self.__onibus.append(onibus)

    def mostrar_relacao_onibus(self):
        print('linha', self.cl)
        for onibus in self.__onibus:
            print(onibus.id)




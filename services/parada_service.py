from services.service_sptrans import ServiceSPTRANS
from typing import List
from entidades.parada import Parada
from services.validador_json import ValidadorJson
from entidades.posicao import Posicao
from entidades.linhas import Linha


class ParadaService(ServiceSPTRANS):

    def __init__(self):
        super().__init__()

    def buscar_paradas_por_linha(self, id_linha: int) -> List[Parada]:
        path = '/Parada/BuscarParadasPorLinha?codigoLinha=' + str(id_linha)
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            lista_paradas = [Parada(*ValidadorJson(parada).validar_json_parada()) for parada in req]
            return lista_paradas

    def buscar_parada_previsao_endereco(self, endereco: str) -> List[Parada]:
        path = '/Parada/Buscar?termosBusca=' + endereco
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            lista_parada = [Parada(*ValidadorJson(parada).validar_json_parada()) for parada in req]
            return self._buscar_previsao_parada(lista_parada)

    def _buscar_previsao_parada(self, lista_parada: List[Parada]):
        for parada in lista_parada:
            path = '/Previsao/Parada?codigoParada=' + str(parada.codigo_parada)

            req = self._sptrans_api.requests_api(path, 'GET')
            parada = Parada(codigo_parada=req['p']['cp'],
                            nome_parada=req['p']['cp'],
                            endereco_localizacao=parada.endereco_localizacao,
                            posicao=Posicao(req['py'], req['px']))
            for linha in req['l']:
                linha = Linha(codigo_identificador=linha['cl'],
                              sentido_linha=linha['sl'],
                              letreiro_numerico=linha['c'].split('-')[0],
                              letreiro_numerico_segunda_parte=int(linha['c'].split('-')[0]),
                              modo_circular=None,
                              terminal_secundario=linha['t1'],
                              terminal_principal=linha['t0']
                              )

            return req

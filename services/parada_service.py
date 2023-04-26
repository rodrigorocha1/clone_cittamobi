from entidades.onibus import Onibus
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
            lista_paradas = [
                Parada(*ValidadorJson(parada).validar_json_parada()) for parada in req]
            return lista_paradas

    def buscar_parada_endereco(self, endereco: str) -> List[Parada]:
        path = '/Parada/Buscar?termosBusca=' + endereco
        if self._login():
            req = self._sptrans_api.requests_api(path, 'GET')
            lista_parada = [
                Parada(*ValidadorJson(parada).validar_json_parada()) for parada in req]
            return lista_parada

    def buscar_previsao_parada(self, codigo_parada: int) -> List[Linha]:
        lista_previsoes = []
        path = '/Previsao/Parada?codigoParada=' + str(codigo_parada)
        req = self._sptrans_api.requests_api(path, 'GET')
        for req_linha in req['p']['l']:
            linha = Linha(
                codigo_identificador=req_linha['cl'],
                sentido_linha=req_linha['sl'],
                letreiro_numerico=req_linha['c'].split('-')[0],
                letreiro_numerico_segunda_parte=(req_linha['c'].split('-')[1]),
                modo_circular=None,
                terminal_secundario=req_linha['lt1'],
                terminal_principal=req_linha['lt0'],

            )

            for req_onibus in req_linha['vs']:
                onibus = Onibus(
                    prefixo=req_onibus['p'],
                    acessibiliade=req_onibus['a'],
                    horario_previsto=req_onibus['t'],
                    posicao=Posicao(req_onibus['py'], req_onibus['px'])
                )
                linha.adicionar_onibus(onibus)
            lista_previsoes.append(linha)
        return lista_previsoes

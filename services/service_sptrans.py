from entidades.linhas import Linha
from services.service_sptrans_api import ServiceSPTRANSAPI
from entidades.parada import Parada
from typing import List
from entidades.onibus import Onibus


class ServiceSPTRANS:
    def __init__(self, ):
        self.__sptrans_api = ServiceSPTRANSAPI()

    def __login(self) -> bool:
        path = '/Login/Autenticar?token='
        req = self.__sptrans_api.requests_api(path)
        return req

    def consultar_linha(self, termo_busca) -> List[Linha]:
        path = '/Linha/Buscar?termosBusca=' + termo_busca
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')
            return [Linha(linha) for linha in req]
        else:
            pass

    def buscar_paradas(self, id_linha: int) -> List[Parada]:
        path = '/Parada/BuscarParadasPorLinha?codigoLinha=' + str(id_linha)
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')
            return [Parada(p) for p in req]

    def buscar_posicoes_veiculos(self, id_linha: int) -> List[Onibus]:
        path = '/Posicao/Linha?codigoLinha=' + str(id_linha)
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')
            req = req['vs']

            return [Onibus(p) for p in req]

    def buscar_previsao_chegada(self, id_linha: int) -> List[Parada]:
        lista_parada = []
        path = '/Previsao/Linha?codigoLinha=' + str(id_linha)
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')
            for parada in req['ps']:
                p = Parada(parada)
                for onibus in parada['vs']:

                    print(onibus)
                    onibus = Onibus(onibus)
                    p.adicionar_onibus(onibus)
                    print(p.nome_parada)
                    print(onibus.posicao.latitude)

                    lista_parada.append(p)

            return lista_parada


if __name__ == '__main__':
    ss = ServiceSPTRANS()
    # a = ss.consultar_linha('8000')
    # print(a[0])
    # a = a[0].codigo_identificador
    # lista_paradas = ss.buscar_paradas(a[0].codigo_identificador)

    lista_paradas = ss.buscar_previsao_chegada(33914)

    for parada in lista_paradas:
        print(parada.nome_parada)
        print(parada.codigo_parada)
        for onibus in parada.mostrar_onibus:
            print(onibus.prefixo)
        print('=====================')

    # for parada in lista_paradas:
    #     print(parada.codigo_parada)
    #     print(parada.endereco_localizacao)
    #     print(parada.nome_parada)
    #     print(parada.posicao.latitude)
    #     print(parada.posicao.longitude)
    #
    #     print('--------------------')
    # print('--------------------')
    # print('--------------------')
    # lista_posicoes_onibus = ss.buscar_posicoes_veiculos(a[0].codigo_identificador)
    # print(lista_posicoes_onibus)
    # for onibus in lista_posicoes_onibus:
    #     print(onibus.prefixo)
    #     print(onibus.acessibiliade)
    #     print(onibus.posicao.latitude)
    #     print(onibus.posicao.latitude)
    #     print('--------------------')

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


if __name__ == '__main__':
    ss = ServiceSPTRANS()
    a = ss.consultar_linha('8000')
    print(a[0])
    lista_paradas = ss.buscar_paradas(a[0].codigo_identificador)

    for parada in lista_paradas:
        print(parada.codigo_parada)
        print(parada.endereco_localizacao)
        print(parada.nome_parada)
        print(parada.posicao.latitude)
        print(parada.posicao.longitude)

        print('--------------------')
    print('--------------------')
    print('--------------------')
    lista_posicoes_onibus = ss.buscar_posicoes_veiculos(a[0].codigo_identificador)
    print(lista_posicoes_onibus)
    for onibus in lista_posicoes_onibus:
        print(onibus.prefixo)
        print(onibus.acessibiliade)
        print(onibus.posicao.latitude)
        print(onibus.posicao.latitude)
        print('--------------------')

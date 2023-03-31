from entidades.linhas import Linha
from services.service_sptrans_api import ServiceSPTRANSAPI
from entidades.parada import Parada
from typing import List
from entidades.onibus import Onibus
import folium


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
                    onibus = Onibus(onibus)
                    p.adicionar_onibus(onibus)
                    lista_parada.append(p)

            return lista_parada


if __name__ == '__main__':
    ss = ServiceSPTRANS()
    linhas = ss.consultar_linha('6055-10')
    print(linhas)
    for linha in linhas:
        print(linha.codigo_identificador)

    for linha in linhas:
        lista_paradas = ss.buscar_paradas(linha.codigo_identificador)
    print(lista_paradas)

    mapa_parada = folium.Map(location=[-23.702749, -46.701907], zoom_start=12)
    for parada in lista_paradas:
        print('lat', parada.posicao.latitude)
        print('lon', parada.posicao.longitude)
        folium.Marker([parada.posicao.longitude, parada.posicao.latitude, ]).add_to(mapa_parada)
    mapa_parada

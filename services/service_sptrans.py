from services.service_sptrans_api import ServiceSPTRANSAPI
import folium
from abc import ABC


class ServiceSPTRANS(ABC):
    def __init__(self):
        self._sptrans_api = ServiceSPTRANSAPI()

    def _login(self) -> bool:
        path = '/Login/Autenticar?token='
        req = self._sptrans_api.requests_api(path)
        return req


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

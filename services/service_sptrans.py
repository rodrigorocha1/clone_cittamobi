from entidades.linhas import Linha
from services.service_sptrans_api import ServiceSPTRANSAPI


class ServiceSPTRANS:
    def __init__(self, ):
        self.__sptrans_api = ServiceSPTRANSAPI()

    def __login(self) -> bool:
        path = '/Login/Autenticar?token='
        req = self.__sptrans_api.requests_api(path)
        return req

    def consultar_linha(self, termo_busca) -> Linha:
        path = '/Linha/Buscar?termosBusca=' + termo_busca
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')
            print(req)

            return [Linha(linha) for linha in req]
        else:
            pass


if __name__ == '__main__':
    ss = ServiceSPTRANS()
    a = ss.consultar_linha('8000')
    print(a[0])

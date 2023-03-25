from entidades.linhas import Linha
from services.service_sptrans_api import ServiceSPTRANSAPI


class ServiceSPTRANS:
    def __init__(self, ):
        self.__sptrans_api = ServiceSPTRANSAPI()

    def __login(self) -> bool:
        path = '/Login/Autenticar?token='
        req = self.__sptrans_api.requests_api(path)
        return req

    def consultar_linha(self) -> Linha:
        path = '/Linha/Buscar?termosBusca=8000'
        if self.__login():
            req = self.__sptrans_api.requests_api(path, 'GET')

            return [Linha(linha) for linha in req]
        else:
            pass


if __name__ == '__main__':
    ss = ServiceSPTRANS()
    a = ss.consultar_linha()
    print(a[0])

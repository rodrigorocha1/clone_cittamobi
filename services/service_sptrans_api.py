import requests


class ServiceSPTRANSAPI:
    def __init__(self):
        self.__url_base = 'http://api.olhovivo.sptrans.com.br/v2.1'
        self.__token = ''
        self.__s = requests.session()

    def requests_api(self, path='/Login/Autenticar?token=', req='POST'):
        if req == 'POST':
            url_completa = self.__url_base + path + self.__token
            response = self.__s.post(url_completa)
        else:
            url_completa = self.__url_base + path
            response = self.__s.get(url_completa)

        return response.json()

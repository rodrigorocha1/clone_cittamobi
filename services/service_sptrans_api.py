import requests
import os
from dotenv import load_dotenv
load_dotenv()


class ServiceSPTRANSAPI:
    def __init__(self):
        """Classe base para todas as requisições
        """
        self.__url_base = 'http://api.olhovivo.sptrans.com.br/v2.1'
        self.__token = os.environ['key']
        self.__s = requests.session()

    def requests_api(self, path='/Login/Autenticar?token=', req='POST'):
        """_summary_

        Args:
            path (str, optional): path da url da api da SPTrans. Defaults to '/Login/Autenticar?token='.
            req (str, optional): requisição GET OU POSTE. Defaults to 'POST'.

        Returns:
            _type_: json da requisição
        """
        if req == 'POST':
            url_completa = self.__url_base + path + self.__token
            response = self.__s.post(url_completa)
        else:
            url_completa = self.__url_base + path
            response = self.__s.get(url_completa)

        return response.json()

import pandas as pd
from typing import List
from entidades.posicao import Posicao
import os


class Trajeto:

    _base_trips = pd.read_csv(
        os.getcwd() + '\\data\\raw\\trips.txt', usecols=['route_id', 'shape_id'])
    _base_shapes = pd.read_csv(os.getcwd() + '\\data\\raw\\shapes.txt',
                               usecols=['shape_id', 'shape_pt_lat', 'shape_pt_lon', 'shape_dist_traveled'])
    _base_completa = _base_trips.merge(
        _base_shapes, on='shape_id', how='inner')
    _base_cor_trajeto = pd.read_csv(
        os.getcwd() + '\\data\\raw\\routes.txt', usecols=['route_id', 'route_color'])

    def __init__(self, nome_linha: str):
        """_summary_

        Args:
            nome_linha (str): nome da linha que faz o traketo
        """

        self.posicoes = self._obter_posicoes(nome_linha)
        self.cor = self._obter_cor_trajeto(nome_linha)

    def _obter_posicoes(self, nome_linha) -> List[Posicao]:
        """
        Método para buscar as posíções da linha
        :param nome_linha: nome da linha
        :return: Uma lista de posições
        """
        try:
            base_filtrada = self._base_completa.loc[
                self._base_completa['route_id'] == nome_linha, ['shape_pt_lat', 'shape_pt_lon']]
            posicoes = base_filtrada.apply(lambda row: Posicao(
                row['shape_pt_lat'], row['shape_pt_lon']), axis=1).tolist()
        except:
            posicoes = ['blue']
        return posicoes

    def _obter_cor_trajeto(self, nome_linha: str) -> str:
        """
        Método para buscar a cor da linha
        :param nome_linha: nome da lina
        :return: a cor da linha
        """
        cor_trajeto = self._base_cor_trajeto[self._base_cor_trajeto['route_id']
                                             == nome_linha]['route_color'].iloc[0]
        return cor_trajeto

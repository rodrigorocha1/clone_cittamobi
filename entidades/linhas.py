from time import sleep
from folium import folium
from entidades.onibus import Onibus
import pandas as pd
from typing import Dict
from entidades.trajeto import Trajeto
from services.service_sptrans import ServiceSPTRANS


class Linha:

    def __init__(self, json_linha: Dict[str, object], quantidade_veiculos=0) -> None:
        self.codigo_identificador = json_linha['cl'] if json_linha.get('cl') is not None else None
        self.modo_circular = json_linha['lc'] if json_linha.get('lc') is not None else None
        self.letreiro_numerico = json_linha['lt'] if json_linha.get('lt') is not None else None
        self.letreiro_numerico_segunda_parte = json_linha['tl'] if json_linha.get('tl') is not None else None
        self.sentido_linha = json_linha['sl'] if json_linha.get('sl') is not None else None
        self.terminal_principal = json_linha['tp'] if json_linha.get('tp') is not None else None
        self.terminal_secundario = json_linha['ts'] if json_linha.get('ts') is not None else None
        self.quantidade_veiculos = quantidade_veiculos
        self.__onibus = []
        self.trajeto = Trajeto(self.letreiro_numerico + '-' +
                                   str(self.letreiro_numerico_segunda_parte))

    def adicionar_onibus(self, onibus: Onibus) -> None:
        self.__onibus.append(onibus)

    @property
    def onibus(self) -> None:
        return self.__onibus

    def __str__(self):
        return str(self.codigo_identificador) + ' ' \
                                                '' + str(self.modo_circular) + ' ' + str(self.letreiro_numerico) + str(
            self.sentido_linha) + ' ' + \
            self.terminal_principal + ' ' + self.terminal_secundario + ' ' + str(
                self.quantidade_veiculos) + self.cor_trajeto

    def atualizar_posicao_onibus(self, linhas):
        ss = ServiceSPTRANS()
        linhas = ss.consultar_linha('8000-10')
        while True:
            mapa_parada = folium.Map(location=[-23.5489, -46.6388], zoom_start=10)

            for linha in linhas:
                lista_posicoes_veiculos = ss.buscar_posicoes_veiculos(linha.codigo_identificador)

                for i in range(len(linha.trajeto.posicoes) - 1):
                    ponto_inicial = [linha.trajeto.posicoes[i].latitude, linha.trajeto.posicoes[i].longitude]
                    ponto_final = [linha.trajeto.posicoes[i + 1].latitude, linha.trajeto.posicoes[i + 1].longitude]
                    folium.PolyLine(locations=[ponto_inicial, ponto_final], color=f'#{linha.trajeto.cor}').add_to(
                        mapa_parada)

                for posicao_veiculo in lista_posicoes_veiculos:
                    folium.Marker([posicao_veiculo.posicao.latitude, posicao_veiculo.posicao.longitude],
                                  popup=posicao_veiculo.prefixo).add_to(mapa_parada)

            paradas = ss.buscar_paradas(linha.codigo_identificador)
            for parada in paradas:
                folium.Marker([parada.posicao.latitude, parada.posicao.longitude], popup=parada.nome_parada).add_to(
                    mapa_parada)

            mapa_parada.save('parada6.html')
            print('Atualizei')
            sleep(10)
from datetime import datetime
from entidades.linhas import Linha
import folium
from services.posicao_veiculo_service import PosicaoVeiculo
from services.parada_service import ParadaService
from entidades.parada import Parada
from typing import List, Tuple
import os
import dash_leaflet as dl


class Mapa:

    def __init__(self):
        self._mapa = None
        self._camino = os.getcwd() + '\\mapas_html\\'

    def _criar_mapa(self, latitude: float, longitude: float):
        return folium.Map(location=[latitude, longitude], zoom_start=14)

    def _desenhar_linha(self, ponto_inicial: List, ponto_final: List, cor: str):
        return folium.PolyLine(locations=[ponto_inicial, ponto_final], color=f'#{cor}')

    def _marcador_mapa(self, latitude: float, longitude: float, popup: str, icon: Tuple):
        return folium.Marker([latitude, longitude],
                             popup=popup,
                             icon=folium.Icon(icon=icon[0], prefix=icon[1], color=icon[2]))

    def _salvar_mapa(self, nome_arquivo_mapa: str):
        self._mapa.save(os.getcwd() + '\\mapas_html\\' + nome_arquivo_mapa)

    def criar_mapa_posicao(self, linhas: Linha):
        pv = PosicaoVeiculo()
        ps = ParadaService()

        for linha in linhas:

            lista_posicoes_veiculos = pv.buscar_posicoes_veiculos(
                linha.codigo_identificador)
            titulo_html = f"""<h1>Mapa da linha {linha.terminal_principal, '-', linha.terminal_secundario}
               </h1><h1>Horário de Referência: {datetime.now().strftime('%HH:%MM:%SS')} </h1>"""

            self._mapa = self._criar_mapa(linha.trajeto.posicoes[len(linha.trajeto.posicoes) // 2].latitude,
                                          linha.trajeto.posicoes[len(linha.trajeto.posicoes) // 2].longitude)

            for i in range(len(linha.trajeto.posicoes) - 1):
                ponto_inicial = [linha.trajeto.posicoes[i].latitude,
                                 linha.trajeto.posicoes[i].longitude]
                ponto_final = [linha.trajeto.posicoes[i + 1].latitude,
                               linha.trajeto.posicoes[i + 1].longitude]
                self._desenhar_linha(
                    ponto_inicial,
                    ponto_final, linha.trajeto.cor
                ).add_to(self._mapa)

            for posicao_veiculo in lista_posicoes_veiculos:
                icon = ('bus', 'fa', 'blue')
                self._marcador_mapa(posicao_veiculo.posicao.latitude, posicao_veiculo.posicao.longitude,
                                    posicao_veiculo.prefixo, icon).add_to(self._mapa)

            paradas = ps.buscar_paradas_por_linha(linha.codigo_identificador)
            icon = ('bus', 'fa', 'red')
            for parada in paradas:
                self._marcador_mapa(parada.posicao.latitude, parada.posicao.longitude, parada.nome_parada,
                                    icon).add_to(self._mapa)
        # mapa_parada.get_root().html.add_child(folium.Element(titulo_html))
        self._salvar_mapa('mapa_linha.html')

    def criar_mapa_paradas(self, paradas: List[Parada]):
        self._mapa = self._criar_mapa(
            paradas[0].posicao.latitude, paradas[0].posicao.longitude)
        icon = ('bus', 'fa', 'red')
        for parada in paradas:
            self._marcador_mapa(
                parada.posicao.latitude, parada.posicao.longitude, parada.codigo_parada, icon).add_to(self._mapa)
        self._salvar_mapa('mapa_previsao.html')

    def criar_mapa_previsao_parada(self, lista_paradas: List[Parada]):
        marcadores_parada = [
            dl.Marker(
                dl.Tooltip(parada.nome_parada),
                position=(
                    parada.posicao.latitude,
                    parada.posicao.longitude
                ),
                id=f"parada_{parada.codigo_parada}")
            for parada in (lista_paradas)]
        return dl.Map(
            [
                dl.TileLayer(),
                *marcadores_parada
            ],
            center=(-23.5505, -46.6333),
            zoom=11,
            id="map",
            style={'width': '100%', 'height': '80vh',
                   'margin': "auto", "display": "block"}
        )

    def __del__(self):
        for nome in os.listdir(self._camino):
            os.remove(self._camino + nome)

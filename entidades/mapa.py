from datetime import datetime
from entidades.linhas import Linha
import folium
from services.posicao_veiculo import PosicaoVeiculo
from services.parada_service import ParadaService
import os


class Mapa:

    def __init__(self):
        self.__mapa = None

    def criar_mapa_posicao(self, linhas: Linha):
        pv = PosicaoVeiculo()
        ps = ParadaService()

        for linha in linhas:

            lista_posicoes_veiculos = pv.buscar_posicoes_veiculos(linha.codigo_identificador)
            titulo_html = f"""<h1>Mapa da linha {linha.terminal_principal, '-', linha.terminal_secundario}
               </h1><h1>Horário de Referência: {datetime.now().strftime('%HH:%MM:%SS')} </h1>"""

            self.__mapa = folium.Map(location=[linha.trajeto.posicoes[len(linha.trajeto.posicoes) // 2].latitude,
                                               linha.trajeto.posicoes[len(linha.trajeto.posicoes) // 2].longitude
                                               ], zoom_start=14)
            for i in range(len(linha.trajeto.posicoes) - 1):
                ponto_inicial = [linha.trajeto.posicoes[i].latitude, linha.trajeto.posicoes[i].longitude]
                ponto_final = [linha.trajeto.posicoes[i + 1].latitude, linha.trajeto.posicoes[i + 1].longitude]
                folium.PolyLine(locations=[ponto_inicial, ponto_final], color=f'#{linha.trajeto.cor}').add_to(
                    self.__mapa)

            for posicao_veiculo in lista_posicoes_veiculos:
                folium.Marker([posicao_veiculo.posicao.latitude, posicao_veiculo.posicao.longitude],
                              popup=posicao_veiculo.prefixo,
                              icon=folium.Icon(icon='bus', prefix='fa', color='blue')).add_to(self.__mapa)

        paradas = ps.buscar_paradas(linha.codigo_identificador)
        for parada in paradas:
            folium.Marker([parada.posicao.latitude, parada.posicao.longitude], popup=parada.nome_parada,
                          icon=folium.Icon(icon='bus', prefix='fa', color='red')).add_to(
                self.__mapa)
        # mapa_parada.get_root().html.add_child(folium.Element(titulo_html))
        self.__mapa.save(os.getcwd() + '\\mapas_html\\mapa_linha.html')

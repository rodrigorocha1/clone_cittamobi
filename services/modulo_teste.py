import folium
from datetime import datetime
from services.service_sptrans import ServiceSPTRANS
from folium import plugins
plugins.Fullscreen

# def criar_mapa(linhas):
#     ss = ServiceSPTRANS()
#
#     for linha in linhas:
#         lista_posicoes_veiculos = ss.buscar_posicoes_veiculos(linha.codigo_identificador)
#         titulo_html = f"""<h1>Mapa da linha {linha.terminal_principal, '-', linha.terminal_secundario}
#         </h1><h1>Horário de Referência: {datetime.now().strftime('%HH:%MM:%SS')} </h1>"""
#
#         mapa_parada = folium.Map(location=[linha.trajeto.posicoes[len(linha.trajeto.posicoes) // 2].latitude,
#                                            linha.trajeto.posicoes[len(linha.trajeto.posicoes) // 2].longitude
#                                            ], zoom_start=14)
#         for i in range(len(linha.trajeto.posicoes) - 1):
#             ponto_inicial = [linha.trajeto.posicoes[i].latitude, linha.trajeto.posicoes[i].longitude]
#             ponto_final = [linha.trajeto.posicoes[i + 1].latitude, linha.trajeto.posicoes[i + 1].longitude]
#             folium.PolyLine(locations=[ponto_inicial, ponto_final], color=f'#{linha.trajeto.cor}').add_to(
#                 mapa_parada)
#
#         for posicao_veiculo in lista_posicoes_veiculos:
#             folium.Marker([posicao_veiculo.posicao.latitude, posicao_veiculo.posicao.longitude],
#                           popup=posicao_veiculo.prefixo,
#                           icon=folium.Icon(icon='bus', prefix='fa', color='blue')).add_to(mapa_parada)
#
#     paradas = ss.buscar_paradas(linha.codigo_identificador)
#     for parada in paradas:
#         folium.Marker([parada.posicao.latitude, parada.posicao.longitude], popup=parada.nome_parada,
#                       icon=folium.Icon(icon='bus', prefix='fa', color='red')).add_to(
#             mapa_parada)
#     #mapa_parada.get_root().html.add_child(folium.Element(titulo_html))
#     plugins.Fullscreen(position='topright', title='Meu Mapa Personalizado').add_to(mapa_parada)
#
#     mapa_parada.save('parada6.html')
#
#
# if __name__ == '__main__':
#     ss = ServiceSPTRANS()
#     linhas = ss.consultar_linha('8000-10')
#
#     criar_mapa(linhas)

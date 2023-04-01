import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import folium
import webbrowser
from time import sleep
from services.modulo_teste import criar_mapa
from services.service_sptrans import ServiceSPTRANS
import os
from entidades.linhas import Linha

ss = ServiceSPTRANS()
linhas = ss.consultar_linha('8000-10')

ss.criar_mapa(linhas)



# app = dash.Dash(__name__)
#
# if not os.path.exists('parada6.html'):
#     with open('parada6.html', 'w', encoding='utf-8') as f:
#         f.write('')
#
# app.layout = html.Div([
#     html.H1('My first app with folium map'),
#     html.Button(id='map-submit-button', n_clicks=0, children='Atualizar Posição'),
#     html.Iframe(id='map', srcDoc=open('parada6.html', 'r', encoding='utf-8').read(), width='100%', height='600'),
# ])
#
#
# @app.callback(
#     dash.dependencies.Output('map', 'srcDoc'),
#     [dash.dependencies.Input('map-submit-button', 'n_clicks')])
# def update_map(n_clicks):
#     if n_clicks is None:
#         return dash.no_update
#     else:
#         ss = ServiceSPTRANS()
#         linhas = ss.consultar_linha('8000-10')
#
#         criar_mapa(linhas)
#         return open('parada6.html', 'r', encoding='utf-8').read()
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

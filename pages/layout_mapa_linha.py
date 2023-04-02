import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import os
from entidades.mapa import Mapa
from services.linha_service import LinhaService

dash.register_page(__name__, path='/', name='Rota Por Linha')


class LayoutMapaLinha:

    @staticmethod
    def __criar_arquivo():
        if not os.path.exists(os.getcwd() + '\\mapas_html\\mapa_linha.html'):
            print('criei')
            with open(os.getcwd() + '\\mapas_html\\mapa_linha.html', 'w', encoding='utf-8') as f:
                f.write('')

    def __init__(self):
        self.__criar_arquivo()
        self.tela = self._get_layout()
        self._calbacks_rota_linha()

    def _get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.InputGroup(
                                [
                                    dbc.Input(id='id_nome_linha',
                                              placeholder='Digite o código da linha'),
                                    dbc.Button('Pesquisar',
                                               id='id_button_pesquisar_linha',
                                               className="class_input_group_container"
                                               )
                                ],
                                className="class_input_group_container",
                                id='id-input-group-mapa-linha'
                            ), style={'margin-top': '10px'}, width={'size': 7, 'offset': 2}
                        ),
                        html.Div('Tire esse html', id='id_div_teste', style={'color': 'black'}),
                    ], id='id_linha_mapa_linha',
                ),
                dbc.Row(
                    [
                        html.P('Lugar aonde vai ficar o mapa', style={'color': 'black'}),
                        html.Iframe(id='map', srcDoc=open(os.getcwd() + '\\mapas_html\\mapa_linha.html', 'r',
                                                          encoding='utf-8').read(), width='100%',
                                    height='600')
                    ], id='id_mapa_linha'
                )
            ], id='id_main_div_mapa_linha'
        )

    def _calbacks_rota_linha(self):
        @callback(
            Output(component_id='map', component_property='srcDoc'),
            State(component_id='id_nome_linha', component_property='value'),
            Input(component_id='id_button_pesquisar_linha', component_property='n_clicks')
        )
        def gerar_mapa(linha: str, n_clicks):
            if n_clicks is None or linha is None:
                dash.no_update
            else:
                ll = LinhaService()
                linhas = ll.consultar_linha(linha)
                m = Mapa()
                m.criar_mapa_posicao(linhas)
                return open(os.getcwd() + '\\mapas_html\\mapa_linha.html', 'r', encoding='utf-8').read()


lml = LayoutMapaLinha()
layout = lml.tela

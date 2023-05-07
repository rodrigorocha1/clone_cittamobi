import atexit
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import os
from entidades.mapa import Mapa
from services.linha_service import LinhaService

dash.register_page(__name__, name='Rota Por Linha', path='/')


class LayoutMapaLinha:

    @staticmethod
    def __criar_arquivo():
        """cria um arquivo ~fake~
        """
        if not os.path.exists(os.getcwd() + '\\mapas_html\\mapa_linha.html'):
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
                                    dbc.Input(
                                        placeholder='Digite o código da Linha Ex: 8000-10',
                                        id='id_nome_linha',
                                    ),
                                    dbc.Button('Pesquisar',
                                               id='id_button_pesquisar_linha',
                                               className="class_input_group_container"
                                               )
                                ],
                                className="class_input_group_container",
                                id='id-input-group-mapa-linha'
                            ), style={'margin-top': '10px'}, width={'size': 7, 'offset': 2}

                        ),
                    ], id='id_linha_mapa_linha',
                ),
                dbc.Row(),
                dbc.Row(
                    [
                        html.Iframe(id='map', srcDoc=open(os.getcwd() + '\\mapas_html\\mapa_linha.html',
                                                          'r',
                                                          encoding='utf-8').read(), width='100%',
                                    height='600'),
                        dcc.Interval(id='interval_component_previsao',
                                     interval=30 * 1000,
                                     n_intervals=0)
                    ], id='id_mapa_linha'
                )
            ], id='id_main_div_mapa_linha'
        )

    def _calbacks_rota_linha(self):

        @callback(
            Output(component_id='map', component_property='srcDoc'),
            State(component_id='id_nome_linha', component_property='value'),
            Input(component_id='id_button_pesquisar_linha',
                  component_property='n_clicks'),
            Input('interval_component_previsao', 'n_intervals')
        )
        def gerar_mapa(linha: str, n_clicks, n_intervals):

            print(linha, n_clicks, n_intervals)
            if n_clicks is None and n_intervals == 0:
                return dash.no_update
            if linha is None or len(linha.strip()) == 0:
                return dash.no_update

            ll = LinhaService()
            linhas = ll.consultar_linha(linha)
            m = Mapa()
            m.criar_mapa_posicao(linhas)
            atexit.register(lambda: m.__del__() if m else None)
            return open(os.getcwd() + '\\mapas_html\\mapa_linha.html', 'r', encoding='utf-8').read()


lml = LayoutMapaLinha()
layout = lml.tela

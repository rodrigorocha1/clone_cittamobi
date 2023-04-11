import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import os
import atexit
from services.parada_service import ParadaService
from entidades.mapa import Mapa

dash.register_page(__name__, name='Parada por Endereços')


class LayoutParadaEndereco:

    @staticmethod
    def __criar_arquivo():
        if not os.path.exists(os.getcwd() + '\\mapas_html\\mapa_previsao.html'):
            with open(os.getcwd() + '\\mapas_html\\mapa_previsao.html', 'w', encoding='utf-8') as f:
                f.write('')

    def __init__(self):
        self.tela = self._get_layout()

    def _get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(

                            dbc.InputGroup(
                                [
                                    dbc.Input(
                                        placeholder='Digite o nome do endereço Ex: USP',
                                        id='id_nome_endereco',
                                    ),
                                    dbc.Button(
                                        'Pesquisar',
                                        id='id_button_pesquisar_previsao',
                                        className="class_input_group_container"
                                    )
                                ],
                                className="class_input_group_container",
                                id='id-input-group-mapa-linha'
                            ),
                            style={'margin-top': '10px'},
                            width={'size': 7, 'offset': 2},
                            id='id_coluna_mapa',
                        )
                    ], id='id_linha_mapa_linha'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Iframe(
                                id='map_previsao',
                                srcDoc=open(os.getcwd() + '\\mapas_html\\mapa_previsao.html',
                                            'r',
                                            encoding='utf-8').read(), width='100%',
                                height='600'),
                            md=10
                        ),
                        dbc.Col(
                            id='id_cards_previsões',
                            md=2
                        ),
                    ]
                )
            ],
            id='id_main_div_pg_end'
        )

    def _calbacks_previsao(self):

        @callback(
            Output(component_id='map_previsao', component_property='srcDoc'),
            State(component_id='id_nome_endereco', component_property='value'),
            Input(component_id='id_button_pesquisar_previsao',
                  component_property='n_clicks'),

        )
        def gerar_mapa(linha: str, n_clicks):
            print(linha, n_clicks)
            if n_clicks is None:
                return dash.no_update
            if linha is None or len(linha.strip()) == 0:
                return dash.no_update

            previsao_parada = ParadaService()
            previsao_paradas = previsao_parada.buscar_parada_previsao_endereco(
                previsao_parada)
            m = Mapa()
            m.criar_mapa_posicao(previsao_paradas)
            atexit.register(lambda: m.__del__() if m else None)
            return open(os.getcwd() + '\\mapas_html\\mapa_previsao.htm', 'r', encoding='utf-8').read()


lpe = LayoutParadaEndereco()
layout = lpe.tela

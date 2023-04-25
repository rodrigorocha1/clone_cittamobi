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
    def _criar_arquivo():
        if not os.path.exists(os.getcwd() + '\\mapas_html\\mapa_previsao.html'):
            with open(os.getcwd() + '\\mapas_html\\mapa_previsao.html', 'w', encoding='utf-8') as f:
                f.write('')

    def __init__(self):
        self._criar_arquivo()
        self.tela = self._get_layout()
        self._calbacks_previsao()

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
                            html.Div(id='my-map'),
                            md=8
                        ),
                        dbc.Col(
                            id='id_cards_previsoes',
                            md=4
                        ),
                    ]
                )
            ],
            id='id_main_div_pg_end'
        )

    def _calbacks_previsao(self):

        @callback(
            Output('my-map', 'children'),
            State(component_id='id_nome_endereco', component_property='value'),
            Input(component_id='id_button_pesquisar_previsao',
                  component_property='n_clicks'),

        )
        def gerar_mapa(endereco: str, n_clicks):

            if n_clicks is None:
                return dash.no_update
            if endereco is None or len(endereco.strip()) == 0:
                return dash.no_update

            previsao_parada = ParadaService()
            previsao_paradas = previsao_parada.buscar_parada_endereco(
                endereco=endereco)
            m = Mapa()
            mapa_parada, marcadores = m.criar_mapa_previsao_parada(
                previsao_paradas)
            return mapa_parada


lpe = LayoutParadaEndereco()
layout = lpe.tela

import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__, name='Parada por Endereços')


class LayoutParadaEndereco:
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
                                        id='id_button_pesquisar_linha',
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
                                id='map',
                                srcDoc=open(os.getcwd() + '\\mapas_html\\mapa_linha.html',
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


lpe = LayoutParadaEndereco()
layout = lpe.tela

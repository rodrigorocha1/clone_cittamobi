import dash
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from typing import List
from services.parada_service import ParadaService
from entidades.mapa import Mapa
from entidades.parada import Parada
from entidades.linhas import Linha
from entidades.onibus import Onibus
import datetime

dash.register_page(__name__, name='Parada por Endereços')


class LayoutParadaEndereco:

    def __init__(self):

        self.tela = self._get_layout()
        self._calbacks_previsao()

    def _gerar_diferenca_minutos(self, horario: str):
        hora2 = datetime.datetime.strptime(horario, '%H:%M').time()
        diferenca = datetime.datetime.combine(datetime.date.today(
        ), hora2) - datetime.datetime.combine(datetime.date.today(), horario)
        diferenca_minutos = diferenca.seconds // 60
        return diferenca_minutos

    def _gerar_cabecalho_tabela_parada(self, lista_paradas: List[Parada]):
        table_header = [
            html.Thead(
                html.Tr(
                    [
                        html.Th(
                            f'Código {parada.codigo_parada}, - {parada.endereco_localizacao} - {parada.nome_parada}',
                            colSpan=3,
                            style={
                                "text-align": "center",
                                'font-size': '12px',
                                'width': '30%'
                            }
                        )
                    ],
                )
            )
            for parada in lista_paradas
        ]
        return table_header

    def _gerar_tabelas_titulo(self, lista_linha: List[Linha]):
        table_header = [
            html.Thead(
                html.Tr(
                    [
                        html.Th(

                            html.Th(
                                f'{linha.codigo_identificador} - {linha.terminal_principal} - {linha.terminal_secundario}',
                                colSpan=3,
                                style={"text-align": "center",
                                       'font-size': '12px',
                                       'width': '30%'}
                            )
                        )
                    ]
                )
            ) for linha in lista_linha
        ]

        return table_header

    def _gerar_tabela_onibus(self, lista_onibus: List[Onibus]):
        TITULOS_CABECALHO = ['Prefixo ônibus',
                             'Previsão Chegada', 'Minutos Faltando']

        cabecalho = [
            html.Thead(
                html.Tr(
                    [
                        html.Th(

                            html.Th(
                                f'{titulos_cabecalho}',
                                colSpan=3,
                                style={"text-align": "center",
                                       'font-size': '12px',
                                       'width': '30%'}
                            )
                        )
                    ]
                )
            ) for titulos_cabecalho in TITULOS_CABECALHO
        ]

        linha = html.Tr(
            [
                html.Td(
                    f'{onibus.prefixo} - {onibus.horario_previsto}',
                    style={
                        'font-size': '12px'
                    }
                ) for onibus in lista_onibus
            ]
        )

        return linha, cabecalho

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
                            html.P(id='saida'),
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
        def gerar_mapa_previsoes(endereco: str, n_clicks):
            if n_clicks is None:
                return dash.no_update
            if endereco is None or len(endereco.strip()) == 0:
                return dash.no_update

            previsao_parada = ParadaService()
            previsao_paradas = previsao_parada.buscar_parada_endereco(
                endereco=endereco)
            m = Mapa()
            mapa_parada = m.criar_mapa_previsao_parada(
                previsao_paradas)
            return mapa_parada
        # callback para gerar previsões por paradda

        @callback(
            Output('saida', 'children'),
            State(component_id='id_nome_endereco', component_property='value'),
            Input(component_id='id_button_pesquisar_previsao',
                  component_property='n_clicks'),
        )
        def gerar_cartoes_previsoes(endereco: str, n_clicks):
            if n_clicks is None:
                return dash.no_update
            if endereco is None or len(endereco.strip()) == 0:
                return dash.no_update,

            previsao_parada = ParadaService()
            paradas_end = previsao_parada.buscar_parada_endereco(
                endereco=endereco)

            previsao_parada_end = map(previsao_parada.buscar_previsao_parada, str(' '.join([
                                      parada_end.codigo_parada for parada_end in paradas_end])))
            return previsao_parada_end


lpe = LayoutParadaEndereco()
layout = lpe.tela

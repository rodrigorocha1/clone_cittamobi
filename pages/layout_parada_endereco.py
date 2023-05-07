import dash
from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc
from services.parada_service import ParadaService
from entidades.mapa import Mapa
from entidades.parada import Parada
from entidades.linhas import Linha

import datetime


dash.register_page(__name__, name='Parada por Endereços')


class LayoutParadaEndereco:

    _hora_atual = datetime.datetime.now().time().strftime('%H:%M')

    def __init__(self):

        self.tela = self._get_layout()
        self._calbacks_previsao()

    def _gerar_diferenca_minutos(self, hora_str: str) -> int:
        hora1 = datetime.datetime.strptime(self._hora_atual, '%H:%M').time()
        hora2 = datetime.datetime.strptime(hora_str, '%H:%M').time()
        diferenca = datetime.datetime.combine(datetime.date.today(
        ), hora2) - datetime.datetime.combine(datetime.date.today(), hora1)
        diferenca_minutos = diferenca.seconds // 60

        return diferenca_minutos

    def _gerar_previsoes_linha(self, linha_previsao_parada: Linha):

        linhas = html.Div(
            [

                html.P(f'{linha_previsao_parada.letreiro_numerico} - {linha_previsao_parada.letreiro_numerico_segunda_parte} - '
                       f'{linha_previsao_parada.terminal_principal} - {linha_previsao_parada.terminal_secundario} ',
                       id=f'id_info_linha_{linha_previsao_parada.codigo_identificador}',
                       className='class_info_linha'
                       ),
                *[
                    html.P(
                        f'{onibus.prefixo} | {onibus.horario_previsto} | {self._gerar_diferenca_minutos(onibus.horario_previsto)} min ',
                        id=f'id_info_onibus_{onibus.prefixo}',
                        className='class_info_onibus'

                    )
                    for onibus in linha_previsao_parada.onibus
                ],
                html.Br()
            ], id=f'id_previsao_linha_{linha_previsao_parada.codigo_identificador}',
            className='class_previsao_linha'
        )
        return linhas

    def _gerar_cartao(self, parada: Parada):
        parada_service = ParadaService()
        linha_previsoes_parada = parada_service.buscar_previsao_parada(
            codigo_parada=parada.codigo_parada)

        card = dbc.Card(
            [
                dbc.CardHeader(
                    f'{parada.codigo_parada} - {parada.endereco_localizacao} - {parada.nome_parada}',
                    id=f'id_cardheader_parada_{parada}',
                    className=f'classheader_parada'
                ),
                dbc.CardBody(
                    [
                        self._gerar_previsoes_linha(linha_previsao_parada)
                        for linha_previsao_parada in linha_previsoes_parada
                    ], id=f'id_cardbody_parada_{parada.codigo_parada}',
                    className='class_cardbody_parada'
                )

            ],
            id=f'id_card_parada_{parada.codigo_parada}',
            className='class_paradas'
        )
        return card

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
                            style={
                                'margin-top': '10px'
                            },
                            width={
                                'size': 7,
                                'offset': 2
                            },
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
                            [
                                html.P(
                                    style={
                                        'color': 'black'
                                    },
                                    id='teste_tempo'
                                ),
                                html.P(
                                    id='saida',
                                    style={
                                        'height': '60%'
                                    }
                                ),
                            ],
                            id='id_cards_previsoes',
                            md=4
                        ),
                        dcc.Interval(
                            id='interval-component',
                            interval=30 * 1000,
                            n_intervals=0)
                    ]
                )
            ],
            id='id_main_div_pg_end'
        )

    def _calbacks_previsao(self):
        @callback(
            Output(component_id='teste_tempo', component_property='children'),
            [
                Input(component_id='interval-component',
                      component_property='n_intervals')
            ]
        )
        def update_time(n):
            return 'Última atualização: ' + str(datetime.datetime.now().time().strftime('%H:%M'))

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

        @callback(
            Output(component_id='saida',
                   component_property='children'),
            State(component_id='id_nome_endereco',
                  component_property='value'),
            Input(component_id='id_button_pesquisar_previsao',
                  component_property='n_clicks'),
            Input(component_id='interval-component',
                  component_property='n_intervals')
        )
        def gerar_cartoes_previsoes(endereco: str, n_clicks, n_intervals):
            if n_clicks is None and n_intervals == 0:
                return dash.no_update
            if endereco is None or len(endereco.strip()) == 0:
                return dash.no_update
            parada_service = ParadaService()
            lista_parada = parada_service.buscar_parada_endereco(
                endereco=endereco)

            layout_cartoes_previsao = html.Div(
                [
                    dbc.Row(
                        self._gerar_cartao(parada),
                        id=f'id_linha_parada_{parada.codigo_parada}',
                        class_name='class_linha_paradas',
                        style={'margin-top': '10px'}
                    ) for parada in lista_parada

                ],
                style={
                    'color': 'black',
                    'overflow-y': 'scroll',
                    'overflow-x': 'hidden',

                    'height': '50%'
                },
                id='id_main_div_paradas',
                className='class_card_paradas'
            )

            return layout_cartoes_previsao


lpe = LayoutParadaEndereco()
layout = lpe.tela

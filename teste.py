from dash import Dash, html
import dash_bootstrap_components as dbc
from typing import List
from services.parada_service import ParadaService
from entidades.parada import Parada
from entidades.linhas import Linha
from entidades.onibus import Onibus

parada_service = ParadaService()
paradas = parada_service.buscar_parada_endereco(endereco='USP')


def gerar_linha_previsao_onibus(lista_onibus: List[Onibus]):
    linha_onibus = html.Tr(
        [
            html.Td(
                f'{onibus.numero_linha} - {onibus.letreiro_numerico}',
                style={'font-size': '12px'}
            ),
            html.Td(
                onibus.terminal_principal,
                style={'font-size': '12px'}
            ),
            html.Td(
                onibus.terminal_secundario,
                style={'font-size': '12px'}
            )
        ] for onibus in lista_onibus
    )
    return linha_onibus


def gerar_tabela(parada: Parada):
    table_header_parada = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        f'Parada {parada.codigo_parada} - Endereço {parada.endereco_localizacao} - Nome {parada.nome_parada}',
                        colSpan=3,
                        style={
                            'text-align': 'center',
                            'font-size': '12px',
                            'width': '50%',
                        }
                    )
                ],
            )
        )
    ]

    previsoes_linha = parada_service.buscar_previsao_parada(
        parada.codigo_parada)

    table_header_previsao = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        f'{previsao_linha.codigo_identificador} -  {previsao_linha.letreiro_numerico} - '
                        f'{previsao_linha.letreiro_numerico_segunda_parte} - {previsao_linha.terminal_principal} - {previsao_linha.terminal_secundario} ',
                        colSpan=3,
                        style={
                            'text-align': 'center',
                            'font-size': '12px',
                            'width': '50%',
                        }
                    )
                ],
            )
        ) for previsao_linha in previsoes_linha
    ]


def gerar_tabelas_cabecalho(lista_parada: List[Parada]):
    cabecalho_hora_atualizacao = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        'Hora última atualização',
                        colSpan=3,
                        style={
                            'text-align': 'center',
                            'font-size': '12px',
                            'width': '30%'
                        }
                    )
                ],
            )
        )
    ]

    table_header = gerar_tabela([parada for parada in lista_parada])

    table_body = [html.Tbody([row1])]

    table = dbc.Table(cabecalho_hora_atualizacao + table_header + table_body,
                      bordered=True,
                      hover=True,
                      responsive=True)
    return table


def gerar_previsao_linhas(linha: Linha):
    pass


table_header = [
    html.Thead(
        html.Tr(
            [
                html.Th(
                    'Hora última atualização',
                    colSpan=3,
                    style={
                        'text-align': 'center',
                        'font-size': '12px',
                        'width': '30%'
                    }
                )
            ],
        )
    ),
    html.Thead(
        html.Tr(
            [
                html.Th(
                    'Parada 450011848 - R TERESA MOUCO DE OLIVEIRA/ R AMANCIO PEDRO DE OLIVEIRA - PARADA HOSPITAL CAMPO LIMPO C/B',
                    colSpan=3,
                    style={
                        'text-align': 'center',
                        'font-size': '12px',
                        'width': '50%',
                    }
                )
            ],
        )
    ),
    html.Thead(
        html.Tr(
            [
                html.Th(
                    '6450 10 TERM. BANDEIRA - TERM. CAPELINHA',
                    colSpan=3,
                    style={'text-align': 'center',
                           'font-size': '12px',
                           'width': '50%'}
                )
            ],
        )
    ),
    html.Thead(
        html.Tr(
            [
                html.Th(
                    'Prefixo ônibus',
                    style={'font-size': '12px'}
                ),
                html.Th(
                    'Previsão Chegada',
                    style={'font-size': '12px'}
                ),
                html.Th(
                    'Minutos Faltando',
                    style={'font-size': '12px'}
                ),
            ],
        )
    )
]

row1 = html.Tr([html.Td('Arthur', style={'font-size': '12px'}), html.Td(
    'Dent', style={'font-size': '12px'}),  html.Td('Dent', style={'font-size': '12px'})])

table_body = [html.Tbody([row1])]

table = dbc.Table(table_header + table_body,
                  bordered=True,
                  hover=True,
                  responsive=True)
app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div(
        [
            dbc.Row(
                '     linha 1',
                style={'color': 'black',
                       'font-size': '12px'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        '1 coluna',
                        style={'color': 'black', 'font-size': '12px'},
                        md=7
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    dbc.Row(
                                        gerar_tabelas_cabecalho(paradas)
                                    )

                                ],
                                style={
                                    'color': 'black',
                                    'overflow-y': 'scroll',
                                    'height': '100%'
                                }
                            ),

                        ],
                        style={'height': '800px'},

                        md=5
                    )
                ]
            )
        ]
    )
])


if __name__ == '__main__':
    app.run(debug=True)

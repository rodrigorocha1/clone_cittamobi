from dash import Dash, html
import dash_bootstrap_components as dbc
from typing import List
from services.parada_service import ParadaService
from entidades.parada import Parada
from entidades.linhas import Linha
from entidades.onibus import Onibus

parada_service = ParadaService()
paradas = parada_service.buscar_parada_endereco(endereco='USP')


def gera_tabela_cabecalho(lista_parada: List[Parada]):
    tabela_cabecalho_hora = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        'Hora última atualização',
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

    tabela_cabecalho_parada = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        f'{parada.codigo_parada} - {parada.endereco_localizacao} - {parada.nome_parada}',
                        style={
                            'text-align': 'center',
                            'font-size': '12px',
                            'width': '30%'
                        }
                    )
                ],
            )
        ) for parada in lista_parada
    ]
    codigo_parada = [parada.codigo_parada for parada in paradas]

    previsoes_parada = parada_service.buscar_previsao_parada(
        codigos_parada=codigo_parada)
    tabela_cabecalho_linha = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        f'{previsao.letreiro_numerico} - {previsao.letreiro_numerico_segunda_parte} \
                        - {previsao.terminal_principal}  - {previsao.terminal_secundario}',
                        style={
                            'text-align': 'center',
                            'font-size': '12px',
                            'width': '30%'
                        }
                    )
                ],
            )
        ) for previsao in previsoes_parada
    ]

    return tabela_cabecalho_hora + tabela_cabecalho_parada + tabela_cabecalho_linha


def gerar_tabela_completa(lista_parada: List[Parada]):
    cabecalho = gera_tabela_cabecalho(lista_parada)
    linhas = gerar_linhas_previsoes(None)
    return cabecalho


def gerar_linhas_previsoes(previsao):

    table_body = [
        html.Tbody(
            [
                html.Tr(
                    [
                        html.Td(
                            'Arthur',
                            style={
                                'font-size': '12px'
                            }
                        )
                    ]
                )
            ]
        )
    ]
    pass


table_header = [
    html.Thead(
        html.Tr(
            [
                html.Th(
                    'Hora última atualização',
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

                    style={'text-align': 'center',
                           'font-size': '12px',
                           'width': '50%'}
                )
            ],
        )
    )
]

row1 = html.Tr(
    [
        html.Td(
            'Arthur',
            style={
                'font-size': '12px'
            }
        )
    ]
)

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
                                        gerar_tabela_completa(paradas)
                                    )

                                ],
                                style={
                                    'color': 'black',
                                    'overflow-y': 'scroll',
                                    'overflow-x': 'hidden',
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

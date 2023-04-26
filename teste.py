from dash import Dash, html
import dash_bootstrap_components as dbc

table_header = [
    html.Thead(
        html.Tr(
            [
                html.Th(
                    "Parada 450011848 - R TERESA MOUCO DE OLIVEIRA/ R AMANCIO PEDRO DE OLIVEIRA - PARADA HOSPITAL CAMPO LIMPO C/B",
                    colSpan=3,
                    style={
                        "text-align": "center"
                    }
                )
            ],
        )
    ),
    html.Thead(
        html.Tr(
            [
                html.Th(
                    "6450 10 TERM. BANDEIRA - TERM. CAPELINHA",
                    colSpan=3,
                    style={"text-align": "center"}
                )
            ],
        )
    ),
    html.Thead(
        html.Tr(
            [
                html.Th(
                    "Prefixo ônibus",
                ),
                html.Th(
                    "Previsão Chegada",
                ),
                html.Th(
                    "Minutos Faltando",
                ),
            ],
        )
    )
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent"),  html.Td("Dent")])

table_body = [html.Tbody([row1])]

table = dbc.Table(table_header + table_body, bordered=True)
app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div(
        [
            dbc.Row(
                '     linha 1',
                style={'color': 'black'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        '1 coluna',
                        style={'color': 'black'},
                        md=8
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    dbc.Row(
                                        table
                                    )
                                    for i in range(1, 10)
                                ],
                                style={
                                    'color': 'black',
                                    'overflow-y': 'scroll',
                                    'height': '100%'
                                }
                            ),

                        ],
                        style={'height': '800px'},

                        md=4
                    )
                ]
            )
        ]
    )
])


if __name__ == '__main__':
    app.run(debug=True)

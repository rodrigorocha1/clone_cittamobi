import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Rota Por Linha')


class LayoutMapaLinha:
    def __init__(self):
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
                    ], id='id_linha_mapa_linha',
                ),
                dbc.Row(
                    [
                        html.P('Lugar aonde vai ficar o mapa', style={'color': 'black'})
                    ], id='id_mapa_linha'
                )
            ], id='id_main_div_mapa_linha'
        )

    def _calbacks_rota_linha(self):
        pass


lml = LayoutMapaLinha()
layout = lml.tela

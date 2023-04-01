import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Rota Por Linha')


class LayoutMapaLinha:
    def __init__(self):
        self.tela = self._get_layout()

    def _get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        html.P('Busca de mapa por linha', style={'color': 'black'})
                    ], id='id_linha_mapa_linha'
                )
            ], id='id_main_div_mapa_linha'
        )


lml = LayoutMapaLinha()
layout = lml.tela

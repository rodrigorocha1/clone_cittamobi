import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Previsão de todas as paradas')


class LayoutTodasParadas:
    def __init__(self):
        self.tela = self._get_layout()

    def _get_layout(self):
        return dbc.Row(
            [
                html.P('LayoutTodasParadas')
            ], id='id_linha_mapa_linha'
        )


ltp = LayoutTodasParadas()
layout = ltp.tela

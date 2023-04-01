from dash import Dash, html, dash
import dash
import dash_bootstrap_components as dbc


class APP:
    '''
        Classe principal para gerar as paginas
    '''

    def __init__(self):
        self.app = Dash(__name__, use_pages=True)
        self.app.tela = self._get_layout()

    def _get_layout(self):
        return html.Div(
            [

            ], id='id_main_div',
            className='class_main_div'
        )

    def rodar_servico(self):
        self.app.run_server(debug=True)


a = APP()
server = a.app.server


if __name__ == '__main__':

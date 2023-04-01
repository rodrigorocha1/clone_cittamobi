from dash import Dash, html, dash
import dash
import dash_bootstrap_components as dbc


class APP:
    """
        Classe principal para gerar as paginas
    """

    def __init__(self):
        self.app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.layout = self._get_layout()

    def _get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.NavbarSimple(
                            children=[
                                dbc.NavLink(pagina["name"], href=pagina["relative_path"]) for pagina in
                                dash.page_registry.values()
                            ]

                        ),
                    ],
                    id='id_barra'
                ),
                dbc.Row(
                    dash.page_container,
                    id='id_container_pages'
                )
            ], id='id_main_div',
            className='class_main_div'
        )

    def rodar_servico(self):
        self.app.run_server(debug=True)


a = APP()
server = a.app.server

for page in dash.page_registry.values():
    print(page["name"], page["path"], page["relative_path"])

if __name__ == '__main__':
    a.rodar_servico()

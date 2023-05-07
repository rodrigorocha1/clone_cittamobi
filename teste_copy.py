from dash import html, dcc
import dash
import datetime
from dash.dependencies import Input, Output
from dash import Dash, html
import dash_bootstrap_components as dbc


app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])


def serve_layout():
    return html.P('The time is: ' + str(datetime.datetime.now().time().strftime('%H:%M')))


app.layout = html.Div([
    html.H1('Live Update Example'),
    html.Div(id='time-div'),
    html.Div(id='interval-div', children=[
        html.P('Atualizando a cada 5 segundos'),
        dcc.Interval(
            id='interval-component',
            interval=5000,  # em milissegundos
            n_intervals=0
        )
    ])
])


@callback(
    Output(component_id='time-div', component_property='children'),
    [Input(component_id='interval-component', component_property='n_intervals')]
)
def update_time(n):
    return 'The time is: ' + str(datetime.datetime.now().time().strftime('%H:%M'))


if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_leaflet as dl
import dash_html_components as html

app = dash.Dash(__name__)


@app.callback(
    dash.dependencies.Output('my-map', 'children'),
    [dash.dependencies.Input('my-button', 'n_clicks')]
)
def update_map(n_clicks):
    # Crie um objeto `dl.Map` com algumas configurações padrão

    # Retorne o mapa encapsulado em um componente HTML
    return dl.Map(
        [
            dl.TileLayer(),
            # line
        ],
        center=(-23.5505, -46.6333),
        zoom=11,
        id="map",
        style={'width': '100%', 'height': '80vh',
               'margin': "auto", "display": "block"}
    )


# Crie uma página com um botão para atualizar o mapa
app.layout = html.Div(
    [
        html.Button('Atualizar Mapa', id='my-button'),
        html.Div(id='my-map')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

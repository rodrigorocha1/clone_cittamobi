import dash
import dash_html_components as html
import dash_leaflet as dl
from dash.dependencies import Input, Output
from services.parada_service import ParadaService

parada_service = ParadaService()
paradas_endereco = parada_service.buscar_parada_endereco('USP')

# print(paradas_endereco)

markers = [
    dl.Marker(dl.Tooltip(parada_endereco.codigo_parada),
              position=(parada_endereco.posicao.latitude, parada_endereco.posicao.longitude),
              id=f"marker_{parada_endereco.codigo_parada}_")
    for parada_endereco in paradas_endereco
    ]

# print(markers)


positions = [(-21.1767, -47.8208, "Ribeirão Preto"),
             (-21.1319, -47.9868, "Sertãozinho")]
markers = [dl.Marker(dl.Tooltip(city), position=(lat, lon), id=f"marker{i}")
           for i, (lat, lon, city) in enumerate(positions)]

line = dl.Polyline(positions=[(lat, lon)
                   for lat, lon, _ in positions], color="red")
app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([
    html.Div(
        dl.Map(
            [
                dl.TileLayer(),
                *markers,
                line
            ],
            center=(-21.1767, -47.8208),
            zoom=11,
            id="map",
            style={'width': '100%', 'height': '80vh',
                   'margin': "auto", "display": "block"}
        )
    ),
    html.Div(id='clickdata')
])
#
# for marker in markers:
#     print(1, marker.children)
#     print(2, marker.id)
#     print(3, marker.__dict__)
#
#
#


@app.callback(Output("clickdata", "children"),
              [Input(marker.id, "n_clicks") for marker in markers])
def marker_click(*args):
    print('args', args)
    print('*args', *args)
    print('args', args)

    print(dash.callback_context.triggered)
    marker_id = dash.callback_context.triggered[0]["prop_id"].split("_")[1]
    print(marker_id, type(marker_id))
    return f"Hello from {marker_id}!"


#
#
if __name__ == '__main__':
    app.run_server(debug=True)

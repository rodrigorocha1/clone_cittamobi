import dash
import dash_html_components as html
import dash_leaflet as dl
from dash.dependencies import Input, Output

positions = [(-21.1767, -47.8208, "Ribeirão Preto"), (-21.1319, -47.9868, "Sertãozinho")]
markers = [dl.Marker(dl.Tooltip(city), position=(lat, lon), id=f"marker{i}")
           for i, (lat, lon, city) in enumerate(positions)]

app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([
    html.Div(dl.Map([dl.TileLayer(), *markers], center=(-21.1544, -47.8208), zoom=11, id="map",
                    style={'width': '100%', 'height': '80vh', 'margin': "auto", "display": "block"})),
    html.Div(id='clickdata')
])


# @app.callback(Output("clickdata", "children"),
#               [Input(marker.id, "n_clicks") for marker in markers])
# def marker_click(*args):
#     print('args', args)
#     print('*args', *args)
#     print('args', args)
#
#     print(dash.callback_context.triggered)
#     marker_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
#     return f"Hello from {marker_id}!"


if __name__ == '__main__':
    app.run_server(debug=True)

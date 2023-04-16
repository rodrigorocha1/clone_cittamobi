import dash
import dash_html_components as html
import dash_leaflet as dl
from dash.dependencies import Input, Output
from services.linha_service import LinhaService
from services.parada_service import ParadaService
from services.posicao_veiculo_service import PosicaoVeiculo

linha_service = LinhaService()
parada_service = ParadaService()
posicao_veiculo = PosicaoVeiculo()

busca_linhas = linha_service.consultar_linha('8000-10')
metade_da_posicao = len(busca_linhas[0].trajeto.posicoes) // 2
# print(busca_linhas)

# print(
#     f'Posição metade: {busca_linhas[0].trajeto.posicoes[metade_da_posicao].latitude}, {busca_linhas[0].trajeto.posicoes[metade_da_posicao].longitude}')


for linha in busca_linhas:
    line = dl.Polyline(
        positions=[
            (posicoes.latitude, posicoes.longitude)
            for posicoes in linha.trajeto.posicoes
        ],
        color=f'#{linha.trajeto.cor}')
#     lista_paradas = parada_service.buscar_paradas_por_linha(
#         linha.codigo_identificador)

#     markers_parada = [
#         dl.Marker(
#             dl.Tooltip(parada.codigo_parada),
#             position=(parada.posicao.latitude,
#                       parada.posicao.longitude),
#             id=f"codigo_parada_{parada.codigo_parada}"
#         )
#         for parada in lista_paradas
#     ]

#     onibus_posicao = posicao_veiculo.buscar_posicoes_veiculos(
#         linha.codigo_identificador)
#     markers_onibus = [
#         dl.Marker(
#             dl.Tooltip(onibus.prefixo),
#             position=(onibus.posicao.latitude,
#                       onibus.posicao.latitude),
#             id=f"codigo_onibus_posicao_{onibus.prefixo}"
#         )
#         for onibus in onibus_posicao
#     ]

# marcadores_completo = markers_parada + markers_onibus
# print(marcadores_completo)
# markers = [
#     dl.Marker(dl.Tooltip(parada_endereco.codigo_parada),
#               position=(parada_endereco.posicao.latitude,
#                         parada_endereco.posicao.longitude),
#               id=f"id_parada_{parada_endereco.codigo_parada}_")
#     for parada_endereco in paradas_endereco
# ]


# positions = [(-21.1767, -47.8208, "Ribeirão Preto"), (-21.1319, -47.9868, "Sertãozinho")]
# markers = [dl.Marker(dl.Tooltip(city), position=(lat, lon), id=f"marker{i}")
#            for i, (lat, lon, city) in enumerate(positions)]


app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div(
    [
        html.Div(
            dl.Map(
                [
                    dl.TileLayer(),

                    line
                ],
                center=(-23.5505, -46.6333),
                zoom=11,
                id="map",
                style={'width': '100%', 'height': '80vh',
                       'margin': "auto", "display": "block"}
            )
        ),
        html.Div(id='clickdata')
    ]
)


# @app.callback(Output("clickdata", "children"),
#               [Input(marker.id, "n_clicks") for marker in markers])
# def marker_click(*args):
#     print('args', args)
#     print('*args', *args)
#     print('args', args)

#     print(dash.callback_context.triggered)
#     marker_id = dash.callback_context.triggered[0]["prop_id"].split("_")[2]
#     print(marker_id, type(marker_id))
#     return f"Hello from {marker_id}"


if __name__ == '__main__':
    app.run_server(debug=True)

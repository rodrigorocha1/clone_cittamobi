from services.parada_service import ParadaService
import dash_leaflet as dl

parada_service = ParadaService()
lista_paradas = parada_service.buscar_parada_endereco('R JOAQUIM NABUCO')

for parada in lista_paradas:
    print(parada.codigo_parada)
    print(parada.posicao.latitude, parada.posicao.longitude)



markers = [dl.Marker(dl.Tooltip(parada.nome_parada), 
                     position=(parada.posicao.latitude, parada.posicao.longitude), 
                     id=f"parada_{parada.codigo_parada}")
                       for parada in (lista_paradas)]
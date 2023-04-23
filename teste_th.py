from services.parada_service import ParadaService

parada_service = ParadaService()

parada_linhas = parada_service.buscar_paradas_por_linha('8000-10')

for parada in parada_linhas:
    print(parada.codigo_parada)
    print(parada.endereco_localizacao)
    print()

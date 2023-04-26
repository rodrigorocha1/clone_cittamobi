from services.parada_service import ParadaService
import dash_leaflet as dl

parada_service = ParadaService()
paradas = parada_service.buscar_parada_endereco(endereco='USP')

for parada in paradas:
    print('-', parada.codigo_parada)
    print('-', parada.endereco_localizacao)
    print('-', parada.nome_parada)
    previsoes_parada = parada_service.buscar_previsao_parada(
        parada.codigo_parada)
    for previsao in previsoes_parada:
        print('--', previsao.codigo_identificador)
        print('--', previsao.terminal_principal)
        print('--', previsao.terminal_secundario)
        for onibus in previsao.onibus:
            print('---', onibus.horario_previsto)
    print()

from services.parada_service import ParadaService
from entidades.parada import Parada
from entidades.posicao import Posicao

ps = ParadaService()
paradas = ps.buscar_parada_previsao_endereco('USP')
for parada in paradas:
    print('primeiro for:', parada.nome_parada, '-', parada.codigo_parada)
    for linha in parada.mostrar_linha:
        print(' segundo for:', linha.codigo_identificador, '-', linha.terminal_principal, '-', linha.terminal_secundario)
        for onibus in linha.onibus:
            print('  terceiro for:', onibus.prefixo)
    print()


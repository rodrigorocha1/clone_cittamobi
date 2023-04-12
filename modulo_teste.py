from services.parada_service import ParadaService
from time import time

tempo_inicial = time()

ps = ParadaService()
previsao_paradas = ps.buscar_parada_previsao_endereco('Carlos')
for parada in previsao_paradas:
    print('-NOME PARADA:', parada.nome_parada, '-', parada.codigo_parada)
    for linha in parada.mostrar_linha:
        print('--CÓDIGO LINHA:', linha.codigo_identificador, '-',
              linha.terminal_principal, '-', linha.terminal_secundario)
        for onibus in linha.onibus:
            print('---PREFIXO:', onibus.prefixo)
            print('---PREVISÃO:', onibus.horario_previsto)
            print('---ACESSIBILIDADE: ', onibus.acessibiliade)
            print()
    print()

tempo_final = time()
duracao = round(tempo_final - tempo_inicial, 2)
print(f'{duracao} Segundos')

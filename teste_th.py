from services.parada_service import ParadaService
import dash_leaflet as dl
import datetime
from time import sleep

hora_atual = datetime.datetime.now().time()

hora_str = hora_atual.strftime('%H:%M')

print(hora_str)

hora1 = datetime.datetime.strptime(hora_str, '%H:%M').time()
hora2 = datetime.datetime.strptime('22:45', '%H:%M').time()

diferenca = datetime.datetime.combine(datetime.date.today(
), hora2) - datetime.datetime.combine(datetime.date.today(), hora1)
diferenca_minutos = diferenca.seconds // 60

# diferenca = datetime.datetime.combine(datetime.date.today(), hora2) - datetime.datetime.combine(datetime.date.today(), hora1)

# print(diferenca)

parada_service = ParadaService()
paradas = parada_service.buscar_parada_endereco(endereco='Morumbi')

codigo_parada = [parada.codigo_parada for parada in paradas]


previsoes_parada = parada_service.buscar_previsao_parada(
    codigos_parada=codigo_parada)


a = [previsao.onibus for previsao in previsoes_parada]
print(a)

# for parada in paradas:
#     print('-', parada.codigo_parada, '-',
#           parada.endereco_localizacao, '-', parada.nome_parada)

#     previsoes_parada = parada_service.buscar_previsao_parada(
#         parada.codigo_parada)
#     for previsao in previsoes_parada:
#         print('--', previsao.codigo_identificador, previsao.letreiro_numerico, previsao.letreiro_numerico_segunda_parte,
#               previsao.terminal_principal, '-', previsao.terminal_secundario)
#         for onibus inr previsao.onibus:

#             hora2 = datetime.datetime.strptime(
#                 onibus.horario_previsto, '%H:%M').time()
#             diferenca = datetime.datetime.combine(datetime.date.today(
#             ), hora2) - datetime.datetime.combine(datetime.date.today(), hora1)
#             diferenca_minutos = diferenca.seconds // 60
#             print('---', onibus.prefixo, '-',
#                   onibus.horario_previsto, '-', hora_str, '-',  diferenca_minutos)
#     print()

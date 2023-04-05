from services.parada_service import ParadaService
from entidades.parada import Parada
from entidades.posicao import Posicao

ps = ParadaService()
paradas = ps.buscar_parada_previsao_endereco('USP')
for parada in paradas:
    print(parada.nome_parada)
    for linha in parada.mostrar_linha:
        print(linha.codigo_identificador)
        for onibus in linha.:
            print(onibus.prefixo)


from services.linha_service import LinhaService
from services.parada_service import ParadaService


linha_service = LinhaService()
ps = ParadaService()

busca_linhas = linha_service.consultar_linha('8000-10')
metade_da_posicao = len(busca_linhas[0].trajeto.posicoes) // 2
print(metade_da_posicao)

for linha in busca_linhas:
    print('linha.codigo_identificador: ', linha.codigo_identificador)
    print('linha.letreiro_numerico: ', linha.letreiro_numerico)
    print('linha.letreiro_numerico_segunda_parte: ',
          linha.letreiro_numerico_segunda_parte)

    print(len(linha.trajeto.posicoes), metade_da_posicao)
    print(linha.trajeto.posicoes[metade_da_posicao].latitude,
          linha.trajeto.posicoes[metade_da_posicao].longitude)
    print()

    for i in range(len(linha.trajeto.posicoes) - 1):

        print('Posições da Linha', linha.terminal_principal,
              '-', linha.terminal_secundario)
        print(linha.trajeto.posicoes[i].latitude,
              linha.trajeto.posicoes[i].longitude)
    paradas = ps.buscar_paradas_por_linha(linha.codigo_identificador)

    for parada in paradas:
        print('paradas')
        print(parada.endereco_localizacao, parada.nome_parada,
              parada.posicao.latitude, parada.posicao.longitude,)

from services.parada_service import ParadaService
from entidades.mapa import Mapa

ps = ParadaService()
paradas = ps.buscar_todas_posicoes_paradas()
m = Mapa()
m.criar_mapa_paradas(paradas)
for parada in paradas:
    print(parada.codigo_parada)
    print(parada.nome_parada)
    print(parada.endereco_localizacao)
    print(parada.posicao.latitude)
    print(parada.posicao.longitude)
    print()

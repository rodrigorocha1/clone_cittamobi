from entidades.linhas import Linha
from entidades.onibus import Onibus
from entidades.parada import Parada
from entidades.posicao import Posicao

posicao = Posicao(1.0, 2.0)
o1 = Onibus(id_onibus=1, posicao=posicao, latitude=1.0, longitude=1.0)
o2 = Onibus(id_onibus=2, posicao=posicao, latitude=1.0, longitude=1.0)
l = Linha(11, 1, 1, 1, 1, 1)
l.adicionar_onibus(o1)
l.adicionar_onibus(o2)
l.mostrar_relacao_onibus()
p = Parada(codigo_parada=1, endereco_localizacao='1', posicao=posicao)

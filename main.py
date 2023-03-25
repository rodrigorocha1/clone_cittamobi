from entidades.linhas import Linha
from entidades.onibus import Onibus

o1 = Onibus(1)
o2 = Onibus(2)
l = Linha(11, 1, 1, 1, 1, 1)
l.adionar_onibus(o1)
l.adionar_onibus(o2)
l.mostrar_relacao_onibus()

from entidades.linhas import Linha
teste = [
    {'cl': 2506, 'lc': False, 'lt': '8000', 'sl': 1, 'tl': 1, 'tp': 'PÇA. RAMOS DE AZEVEDO', 'ts': 'TERM. LAPA'},
    {'cl': 2506, 'lc': False, 'lt': '8000', 'sl': 1, 'tl': 1, 'tp': 'PÇA. RAMOS DE AZEVEDO', 'ts': 'TERM. LAPA'}
]
lista = [Linha(t) for t in teste]

print(lista)
print(lista[0].codigo_identificador)
print(lista[1].codigo_identificador)
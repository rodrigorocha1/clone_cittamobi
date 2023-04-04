import os
import pandas as pd

base_linhas = pd.read_csv(os.getcwd() + '\\data\\raw\\routes.txt')
print(base_linhas['route_id'].str.split('-').values)

for indice, linha in base_linhas.iterrows():
    print(linha['route_id'])

print([(linha['route_id'], linha['route_id'][0], linha['route_id'][1]) for indice, linha in base_linhas.iterrows()])

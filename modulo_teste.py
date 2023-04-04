import os
import pandas as pd

base_linhas = pd.read_csv(os.getcwd() + '\\data\\raw\\routes.txt')
print(base_linhas['route_id'].str.split('-').values)

for indice, linha in base_linhas.iterrows():
    try:
        print(linha['route_id'].split('-')[0], linha['route_id'].split('-')[1])
    except IndexError:
        print(linha['route_id'])

print([(route_id_parts[0], route_id_parts[1]) if len(route_id_parts) == 2 else route_id_parts for route_id_parts in
       [linha['route_id'].split('-') for _, linha in base_linhas.iterrows()]])

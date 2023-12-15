import pandas as pd

file = '/workspaces/api-bolsa/Dados_BVSP_20231214_024249.txt'

df = pd.read_csv(file)
print(df)

path_file = '/workspaces/api-bolsa/'
name_file = 'dados_teste.txt'

df.to_csv(f'{path_file}{name_file}', sep=';')
print('Arquivo salvo!')
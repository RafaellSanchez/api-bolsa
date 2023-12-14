import pandas as pd

file = '/workspaces/api-bolsa/data/bovespa/Dados_BVSP_20231214_024249.txt'

df = pd.read_csv(file)
print(df)

path_file = '/workspaces/api-bolsa/path_scheduler/'
name_file = 'dados_teste.txt'

df.to_csv(f'{path_file}{name_file}', sep=';')
print('Arquivo salvo!')
import pandas as pd 
import json as js
import requests

#teste

path = '/workspaces/api-bolsa/Dados_BVSP_20231214_024249.txt'

df = pd.read_csv(path, header=True)
print(df)
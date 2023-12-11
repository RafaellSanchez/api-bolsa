import pandas as pd
import sqlite3

file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231209_170916.csv'

df = pd.read_csv(file, delimiter=';')
# print(df)

destino = '/workspaces/api-bolsa/database/db/dtbase_moeda.sqlite'
conn = sqlite3.connect(destino)
cur = conn.cursor()

df.to_sql('tb_moeda', conn, if_exists='append', index=False)

cur.execute("SELECT Date FROM tb_moeda;")
rows = cur.fetchall()


for row in rows:
    print(row)


cur.close()
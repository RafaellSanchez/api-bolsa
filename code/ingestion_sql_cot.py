import sqlite3
import pandas as pd

file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231210_200000.csv'

# df = pd.read_csv(file, delimiter=';')
# Especifique o parâmetro index_col=False para evitar que o pandas interprete a primeira coluna como índice
df = pd.read_csv(file, delimiter=';', index_col=False)

destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
conn = sqlite3.connect(destino)
cur = conn.cursor()

# Variável para contar as inserções
insercoes = 0

for index, row in df.iterrows():
    dt_igtao = row['dt_igtao']
    cur.execute("SELECT COUNT(*) FROM tb_cotMoeda WHERE dt_igtao = ?", (dt_igtao,))
    data_exists = cur.fetchone()[0]

    # Se não houver registro com a mesma data, insere na tabela
    if data_exists == 0:
        values_to_insert = (row['Unnamed: 0'], row['USDBRL'], row['EURBRL'], row['BTCBRL'], row['USDBRLT'], row['dt_igtao'])
        cur.execute("INSERT INTO tb_cotMoeda (Unnamed_0, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)
        insercoes += 1  # Incrementa o contador de inserções


conn.commit()

print(f"{insercoes} linhas foram inseridas no banco de dados.")

cur.execute("SELECT * FROM tb_cotMoeda;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
























# import sqlite3
# import pandas as pd



# file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231211_234723.csv'

# df = pd.read_csv(file, delimiter=';')
# # print(df)

# destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
# conn = sqlite3.connect(destino)
# cur = conn.cursor()

# df.to_sql('tb_cotMoeda', conn, if_exists='append', index=False)

# cur.execute("SELECT * FROM tb_cotMoeda;")
# rows = cur.fetchall()


# for row in rows:
#     print(row)


# cur.close()
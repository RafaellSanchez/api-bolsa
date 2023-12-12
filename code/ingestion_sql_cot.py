import sqlite3
import pandas as pd

file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231210_200000.csv'

df = pd.read_csv(file, delimiter=';')

destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
conn = sqlite3.connect(destino)
cur = conn.cursor()

# Variável para contar as inserções
insercoes = 0

# Verifica cada linha do DataFrame antes de inserir na tabela
for index, row in df.iterrows():
    dt_igtao = row['dt_igtao']
    cur.execute("SELECT COUNT(*) FROM tb_cotMoeda WHERE dt_igtao = ?", (dt_igtao,))
    data_exists = cur.fetchone()[0]

    # Se não houver registro com a mesma data, insere na tabela
    if data_exists == 0:
        cur.execute("INSERT INTO tb_cotMoeda VALUES (Unnamed:0, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao)")  # Substitua ... pelos valores do DataFrame
        # Insira os valores correspondentes na instrução SQL acima
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
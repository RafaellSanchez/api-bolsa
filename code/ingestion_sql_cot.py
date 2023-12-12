import sqlite3
import pandas as pd

def carregar_dados_completos():
    file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231212_004236.csv'
    df = pd.read_csv(file, delimiter=';', index_col=False)

    destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
    conn = sqlite3.connect(destino)
    cur = conn.cursor()

    # Cria a tabela se ela não existir
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS tb_cotMoeda (
            NomeIndice VARCHAR(10),
            USDBRL FLOAT,
            EURBRL FLOAT,
            BTCBRL FLOAT,
            USDBRLT FLOAT,
            dt_igtao DATE,
            CONSTRAINT unique_date UNIQUE (dt_igtao) -- Garante unicidade na coluna dt_igtao
        );
    ''')

    # Insere todos os dados do CSV, ignorando se já existem na tabela ou não
    for _, row in df.iterrows():
        values_to_insert = (
            row['NomeIndice'], row['USDBRL'], row['EURBRL'], 
            row['BTCBRL'], row['USDBRLT'], row['dt_igtao']
        )
        cur.execute("INSERT OR IGNORE INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)

    conn.commit()
    conn.close()

# Carga inicial completa
carregar_dados_completos()






# import sqlite3
# import pandas as pd

# def carregar_dados_completos():
#     file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231212_004236.csv'
#     df = pd.read_csv(file, delimiter=';', index_col=False)

#     destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
#     conn = sqlite3.connect(destino)
#     cur = conn.cursor()

#     # Cria a tabela se ela não existir
#     cur.execute(''' 
#         CREATE TABLE IF NOT EXISTS tb_cotMoeda (
#             NomeIndice VARCHAR(10),
#             USDBRL FLOAT,
#             EURBRL FLOAT,
#             BTCBRL FLOAT,
#             USDBRLT FLOAT,
#             dt_igtao DATE,
#             CONSTRAINT unique_date UNIQUE (dt_igtao) -- Garante unicidade na coluna dt_igtao
#         );
#     ''')

#     # Insere todos os dados do CSV, ignorando se já existem na tabela ou não
#     cur.executemany("INSERT OR IGNORE INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", df.values.tolist())

#     conn.commit()
#     conn.close()

# def inserir_novos_registros():
#     file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231212_004236.csv'
#     df = pd.read_csv(file, delimiter=';', index_col=False)

#     destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
#     conn = sqlite3.connect(destino)
#     cur = conn.cursor()

#     for index, row in df.iterrows():
#         dt_igtao = row['dt_igtao']
#         cur.execute("SELECT COUNT(*) FROM tb_cotMoeda WHERE dt_igtao = ?", (dt_igtao,))
#         data_exists = cur.fetchone()[0]

#         # Se não houver registro com a mesma data, insere na tabela
#         if data_exists == 0:
#             values_to_insert = (row['NomeIndice'], row['USDBRL'], row['EURBRL'], row['BTCBRL'], row['USDBRLT'], row['dt_igtao'])
#             cur.execute("INSERT INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)

#     conn.commit()
#     conn.close()

# # Carga inicial completa
# carregar_dados_completos()

# # Inserir novos registros
# inserir_novos_registros()


























# # import sqlite3
# # import pandas as pd

# # file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231212_004236.csv'
# # df = pd.read_csv(file, delimiter=';', index_col=False)

# # destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
# # conn = sqlite3.connect(destino)
# # cur = conn.cursor()

# # # Verifica se a tabela já existe, se não existir, cria a tabela
# # cur.execute(''' 
# #     CREATE TABLE IF NOT EXISTS tb_cotMoeda (
# #         NomeIndice VARCHAR(10),
# #         USDBRL FLOAT,
# #         EURBRL FLOAT,
# #         BTCBRL FLOAT,
# #         USDBRLT FLOAT,
# #         dt_igtao DATE,
# #         CONSTRAINT unique_date UNIQUE (dt_igtao) -- Garante unicidade na coluna dt_igtao
# #     );
# # ''')

# # insercoes = 0

# # for index, row in df.iterrows():
# #     dt_igtao = row['dt_igtao']
# #     cur.execute("SELECT COUNT(*) FROM tb_cotMoeda WHERE dt_igtao = ?", (dt_igtao,))
# #     data_exists = cur.fetchone()[0]

# #     # Se não houver registro com a mesma data, insere na tabela
# #     if data_exists == 0:
# #         values_to_insert = (row['NomeIndice'], row['USDBRL'], row['EURBRL'], row['BTCBRL'], row['USDBRLT'], row['dt_igtao'])
# #         cur.execute("INSERT INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)
# #         insercoes += 1

# # conn.commit()

# # print(f"{insercoes} linhas foram inseridas no banco de dados.")

# # cur.execute("SELECT * FROM tb_cotMoeda;")
# # rows = cur.fetchall()

# # for row in rows:
# #     print(row)

# # cur.close()























# # import sqlite3
# # import pandas as pd

# # file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231211_211723.csv'
# # df = pd.read_csv(file, delimiter=';', index_col=False)

# # destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
# # conn = sqlite3.connect(destino)
# # cur = conn.cursor()

# # # Verifica se a tabela já existe, se não existir, cria a tabela
# # cur.execute(''' 
# #     CREATE TABLE IF NOT EXISTS tb_cotMoeda (
# #         NomeIndice VARCHAR(10),
# #         USDBRL FLOAT,
# #         EURBRL FLOAT,
# #         BTCBRL FLOAT,
# #         USDBRLT FLOAT,
# #         dt_igtao DATE,
# #         CONSTRAINT unique_date UNIQUE (dt_igtao) -- Garante unicidade na coluna dt_igtao
# #     );
# # ''')

# # insercoes = 0

# # for index, row in df.iterrows():
# #     values_to_insert = (row['NomeIndice'], row['USDBRL'], row['EURBRL'], row['BTCBRL'], row['USDBRLT'], row['dt_igtao'])
# #     cur.execute("INSERT OR IGNORE INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)
# #     insercoes += 1

# # conn.commit()

# # print(f"{insercoes} linhas foram inseridas no banco de dados.")

# # cur.execute("SELECT * FROM tb_cotMoeda;")
# # rows = cur.fetchall()

# # for row in rows:
# #     print(row)

# # cur.close()





















# # import sqlite3
# # import pandas as pd

# # file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231212_004236.csv'
# # df = pd.read_csv(file, delimiter=';', index_col=False)

# # destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
# # conn = sqlite3.connect(destino)
# # cur = conn.cursor()

# # # Verifica se a tabela já existe, se não existir, cria a tabela
# # cur.execute(''' 
# #     CREATE TABLE IF NOT EXISTS tb_cotMoeda (
# #         NomeIndice VARCHAR(10),
# #         USDBRL FLOAT,
# #         EURBRL FLOAT,
# #         BTCBRL FLOAT,
# #         USDBRLT FLOAT,
# #         dt_igtao DATE,
# #         CONSTRAINT unique_date UNIQUE (dt_igtao) -- Garante unicidade na coluna dt_igtao
# #     );
# # ''')

# # insercoes = 0

# # for index, row in df.iterrows():
# #     dt_igtao = row['dt_igtao']
# #     cur.execute("SELECT COUNT(*) FROM tb_cotMoeda WHERE dt_igtao = ?", (dt_igtao,))
# #     data_exists = cur.fetchone()[0]

# #     # Verifica se a data já existe na tabela, se não existir, insere
# #     if data_exists == 0:
# #         values_to_insert = (row['NomeIndice'], row['USDBRL'], row['EURBRL'], row['BTCBRL'], row['USDBRLT'], row['dt_igtao'])
# #         cur.execute("INSERT INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)
# #         insercoes += 1

# # conn.commit()

# # print(f"{insercoes} linhas foram inseridas no banco de dados.")

# # cur.execute("SELECT * FROM tb_cotMoeda;")
# # rows = cur.fetchall()

# # for row in rows:
# #     print(row)

# # cur.close()




















# # import sqlite3
# # import pandas as pd

# # file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231212_004236.csv'

# # # df = pd.read_csv(file, delimiter=';')
# # # Especifique o parâmetro index_col=False para evitar que o pandas interprete a primeira coluna como índice
# # df = pd.read_csv(file, delimiter=';', index_col=False)

# # destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
# # conn = sqlite3.connect(destino)
# # cur = conn.cursor()

# # cur.execute(''' CREATE TABLE tb_cotMoeda (
# #     NomeIndice VARCHAR(10),
# #     USDBRL FLOAT,
# #     EURBRL FLOAT,
# #     BTCBRL FLOAT,
# #     USDBRLT FLOAT,
# #     dt_igtao DATE
# # );
# #             ''')


# # # Variável para contar as inserções
# # insercoes = 0

# # for index, row in df.iterrows():
# #     dt_igtao = row['dt_igtao']
# #     cur.execute("SELECT COUNT(*) FROM tb_cotMoeda WHERE dt_igtao = ?", (dt_igtao,))
# #     data_exists = cur.fetchone()[0]

# #     # Se não houver registro com a mesma data, insere na tabela
# #     if data_exists == 0:
# #         values_to_insert = (row['NomeIndice'], row['USDBRL'], row['EURBRL'], row['BTCBRL'], row['USDBRLT'], row['dt_igtao'])
# #         cur.execute("INSERT INTO tb_cotMoeda (NomeIndice, USDBRL, EURBRL, BTCBRL, USDBRLT, dt_igtao) VALUES (?, ?, ?, ?, ?, ?)", values_to_insert)
# #         insercoes += 1  # Incrementa o contador de inserções


# # conn.commit()

# # print(f"{insercoes} linhas foram inseridas no banco de dados.")

# # cur.execute("SELECT * FROM tb_cotMoeda;")
# # rows = cur.fetchall()

# # for row in rows:
# #     print(row)

# # cur.close()
























# # # import sqlite3
# # # import pandas as pd



# # # file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231211_234723.csv'

# # # df = pd.read_csv(file, delimiter=';')
# # # # print(df)

# # # destino = '/workspaces/api-bolsa/database/db/dtbase_cotacaoMoeda.sqlite'
# # # conn = sqlite3.connect(destino)
# # # cur = conn.cursor()

# # # df.to_sql('tb_cotMoeda', conn, if_exists='append', index=False)

# # # cur.execute("SELECT * FROM tb_cotMoeda;")
# # # rows = cur.fetchall()


# # # for row in rows:
# # #     print(row)


# # # cur.close()
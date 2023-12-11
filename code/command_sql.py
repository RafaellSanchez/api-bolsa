import os
import pandas as pd
import sqlite3

# Diretório contendo os arquivos CSV
diretorio_txt = '/workspaces/api-bolsa/data/moeda'

# Arquivo SQLite onde você deseja armazenar os dados
caminho_banco_dados = '/workspaces/api-bolsa/database/db/tb_acoes.sqlite'

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(caminho_banco_dados)

# Listar os arquivos TXT no diretório
arquivos_txt = [arquivo for arquivo in os.listdir(diretorio_txt) if arquivo.endswith('.txt')]

# Para cada arquivo TXT, criar uma tabela correspondente no banco de dados e inserir os dados
for arquivo in arquivos_txt:
    nome_tabela = os.path.splitext(arquivo)[0]  # Nome da tabela será o nome do arquivo sem extensão
    caminho_arquivo_txt = os.path.join(diretorio_txt, arquivo)
    
    # Ler o arquivo TXT usando o Pandas com delimitador de espaço
    df = pd.read_csv(caminho_arquivo_txt, delimiter='\t', engine='python')
    
    # Inserir os dados do arquivo TXT na tabela correspondente no banco de dados
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()






# file = '/workspaces/api-bolsa/data/moeda/cotacao_atual_20231209_170916.csv'

# df = pd.read_csv(file, delimiter=';')
# # print(df)

# destino = '/workspaces/api-bolsa/database/db/dtbase_moeda.sqlite'
# conn = sqlite3.connect(destino)
# cur = conn.cursor()

# df.to_sql('tb_moeda', conn, if_exists='append', index=False)

# cur.execute("SELECT Date FROM tb_moeda;")
# rows = cur.fetchall()


# for row in rows:
#     print(row)


# cur.close()
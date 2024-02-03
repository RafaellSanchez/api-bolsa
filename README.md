# api-bolsa
Está é uma Api que será consumida os dados da bolsa de valores


Este repositório é um projeto de Engenharia de Dados, será consumido dados atravez de uma api com o intuito de monitorar os dados diários da bolsa de valores e onde são realizados processos de ETL (Extract, Transform, Load) para analisar e manipular os dados


Funcionalidades Principais:

Extração de Dados: Coleta dos resultados da Mega Sena de fontes oficiais.
Transformação de Dados: Aplicação de limpezas, formatações e cálculos nos resultados.
Carregamento: Armazenamento dos dados processados em um formato estruturado.

Técnologias Utilizadas:

Python para a manipulação e análise de dados.
Pandas para realizar as transformações nos conjuntos de dados.
SQL para consulta ou armazenamento em bancos de dados.

Estrutura do Repositório:

/code: Contém os scripts Python para ETL.
/data: Armazena os dados brutos e processados.
/docs: Documentação do projeto e instruções de uso.

## Repos

> - bckp
> - code
> - data
> - database
> - doc
> - .gitignore
> - README.md


### Repositorio 'bckp':

> ### beckp:
> - api_bolsa.py
> - Dados_BVSP_20231214_024249.txt
> - dados_teste.txt
> - file_teste.py
> - teste_scheduler.py

### Respositorio 'code':

> ### code:
> - api_bolsa.py
> - api_cotacao.py
> - api_empr.py
> - command_sql.py
> - ingestion_sql_cot.py
> - ingestion_teste.ipynb
> - mv_file_ingestion.py
> - teste_sqlite.ipynb
> - teste.py

### Repositorio 'data': 


> ### acoes:
> - Dados_VALE3.SA_20231211_025320.txt
> - Dados_VALE3.SA_20231209_165006.txt
> - Dados_PETR4.SA_20231211_025320.txt
> - Dados_PETR4.SA_20231209_165005.txt
> - Dados_ITUB4.SA_20231211_025320.txt
> - Dados_ITUB4.SA_20231209_165005.txt
> - Dados_BBDC4.SA_20231209_165006.txt
> - Dados_ABEV3.SA_20231209_165005.txt

> ### bovespa:
> - Dados_BVSP_20231209_164453.txt
> - Dados_BVSP_20231210_233856.txt
> - Dados_BVSP_20231214_024124.txt
> - Dados_BVSP_20231214_024249.txt

> ### moeda:
 > - cotacao_atual_20231210_200000.csv
 > - cotacao_atual_20231212_004236.csv
 > - cotacao_atual_20231211_234723.csv
 > - cotacao_atual_20231211_211723.csv
 > - cotacao_atual_20231211_024451.csv
 > - cotacao_atual_20231209_170916.csv


### Repositorio 'database':

> ### archiving:
> - Dados_PETR4.SA_20231209_165005.txt
> - Dados_VALE3.SA_20231209_165006.txt
> - Dados_ITUB4.SA_20231209_165005.txt
> - Dados_BVSP_20231210_233856.txt
> - Dados_BBDC4.SA_20231209_165006.txt
> - Dados_ABEV3.SA_20231209_165005.txt
> - cotacao_atual_20231209_170916.csv


> ### db:
> - dtbase_bolsa.sqlite
> - dtbase_cotacaoMoeada.sqlite
> - dtbase_moeada.sqlite
> - tb_acoes.sqlite

### Repositorio 'doc':
> - projeto api-bolsa-1.pdf
> - doc_moeda.txt
> - doc_git.txt
> - doc_bolsa.txt
> - arquitetura_api-bolsa.drawio.html




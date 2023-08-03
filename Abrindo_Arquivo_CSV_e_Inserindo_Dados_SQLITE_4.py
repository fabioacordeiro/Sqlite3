import csv
import sqlite3
from pathlib import Path

import pandas as pd

# abrindo o arquivo CSV e mostrando 5 linhas.
# skiprows => informar quais as linhas que serão ignoradas
# nrows => qual a quantidade de linhas que serão percorridas
# usecols => qual as colunas que serão utilizadas
'''
BD = pd.read_csv('C:/fabio/Python/Carrefour/CTE.csv',
                 sep='|', nrows=5, skiprows=[0, 1], usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 28, 30, 31, 32], low_memory=False)
'''
BD = pd.read_csv('C:/fabio/Python/Carrefour/CTE.csv',
                 sep='|', nrows=5, skiprows=[1], usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 28, 30, 31, 32], low_memory=False)
# print(BD)
# BD.to_excel('BD.xlsx')
# BD.to_csv('BD.csv')

TABLE_NAME = 'CTE_teste_2'

ROOT_DIR = Path(__file__).parent
DB_NAME = 'Carrefour.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
'''
cursor.execute(
    f'DELETE FROM "{TABLE_NAME}"'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
'''

# Criando a tabela no SQLite3
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'CTE INTEGER PRIMARY KEY,'  # 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'Peso REAL,'
    'Dt_Emissao Date,'
    'uf_destino TEXT,'
    'uf_origem TEXT,'
    'Cidade_Destino TEXT,'
    'CO_Origem TEXT,'
    'CO_Destino TEXT,'
    'CEP TEXT,'
    'Tarifa TEXT,'
    'Opcao_Entrega TEXT,'
    'Valor_Dec REAL,'
    'ad_valorem REAL,'
    'Coleta TEXT,'
    'Embalagem TEXT,'
    'Entrega TEXT,'
    'icms REAL,'
    'TX_entrega_Central REAL,'
    'TX_entrega_Destino REAL,'
    'TX_entrega_Origem REAL,'
    'FOB REAL,'
    'Frete REAL,'
    'Gris REAL,'
    'Interior TEXT,'
    'Reversa TEXT,'
    'TDE REAL,'
    'Faturamento REAL,'
    'Conta_Corrente TEXT,'
    'CNPJ_tomador TEXT,'
    'CNPJ_remetente TEXT,'
    'Produto TEXT,'
    'Razao_Social TEXT'
    ')'
)

# Inserindo os dados no SQLite3
BD.to_sql(
    name='CTE_teste_2',
    con=connection,
    if_exists='replace',
    index=False,
    dtype={
        'CTE': 'INTEGER',
        'Peso': 'TEXT',
        'Dt_Emissao': 'Date',
        'uf_destino': 'TEXT',
        'uf_origem': 'TEXT',
        'Cidade_Destino': 'TEXT',
        'CO_Origem': 'TEXT',
        'CO_Destino': 'TEXT',
        'CEP': 'TEXT',
        'Tarifa': 'TEXT',
        'Opcao_Entrega': 'TEXT',
        'Valor_Dec': 'REAL',
        'ad_valorem': 'REAL',
        'Coleta': 'TEXT',
        'Embalagem': 'TEXT',
        'Entrega': 'TEXT',
        'icms': 'REAL',
        'TX_entrega_Central': 'REAL',
        'TX_entrega_Destino': 'REAL',
        'TX_entrega_Origem': 'REAL',
        'FOB': 'REAL',
        'Frete': 'REAL',
        'Gris': 'REAL',
        'Interior': 'TEXT',
        'Reversa': 'TEXT',
        'TDE': 'REAL',
        'Faturamento': 'REAL',
        'Conta_Corrente': 'TEXT',
        'CNPJ_tomador': 'TEXT',
        'CNPJ_remetente': 'TEXT',
        'Produto': 'TEXT',
        'Razao_Social': 'TEXT'
    }
)


'''

with open(BD, 'r') as file:
    csv_reader = csv.reader(file)
    no_records = 0
    for line in csv_reader:
        cursor.execute(
            'INSERT INTO CTE_teste_3 (id, CTE, Peso) VALUES (null, ? ,?)')
        connection.commit()
        no_records += 1
print('\n')
print(f'{no_records} Quantidade de dados inseridos..')
'''
'''
    no_records = 0
    for row in file:
        cursor.executemany(
            'INSERT INTO CTE_teste_3 (id, CTE, Peso) VALUES (null, ? ,?)', row.split(';'))
        connection.commit()
        no_records += 1
connection.close()
print('\n')
'''
'''

print(60*'-')
print(f'{"Inseir via SQL":^60}')
BD.to_sql(
    name={TABLE_NAME},
    con=connection,
    if_exists='replace',
    index=False,
    dtype={'CTE': 'TEXT',
           'Peso': 'TEXT'
           }
)
'''
connection.close()
# cursor.execute  #Para um unico valor
# cursor.executemany  #Para muitos valores

connection.commit()
cursor.close()
connection.close()

# '''

print('Fim')

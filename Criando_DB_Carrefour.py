import sqlite3
from pathlib import Path

import pandas as pd

# abrindo o arquivo CSV e mostrando 5 linhas.
# Exemplo de uso de lambda
# pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ["COL1", "COL3"])
# mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
# mtcars.head()

# Access a row by numerical index with .iloc
# mtcars.iloc[2]


# BD = pd.read_csv('C:/fabio/Python/Carrefour/CTE.csv', sep='|',nrows=2 ,usecols=[1,], low_memory=False)

# abrindo o arquivo CSV e mostrando 2 linhas.
BD = pd.read_csv('C:/fabio/Python/Carrefour/CTE.csv',
                 sep='|', nrows=5, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 28, 30, 31, 32], low_memory=False)
# pd.options.display.max_rows = 5
BD.describe()
BD.info(memory_usage=dict)
print(BD)

TABLE_NAME = 'CTE_teste'

ROOT_DIR = Path(__file__).parent
DB_NAME = 'Carrefour.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()
# CUIDADO: fazendo delete sem where
'''
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
'''

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'CTE TEXT,'
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


connection.commit()
cursor.close()
connection.close()


print('Fim')

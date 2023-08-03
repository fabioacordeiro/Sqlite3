import sqlite3
from pathlib import Path

import pandas as pd

# import statsmodels.api as sm  #(To access mtcars dataset)


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
                 sep='|', nrows=2, low_memory=False)
# pd.options.display.max_rows = 5
BD.describe()
BD.info(memory_usage=dict)
'''
TABLE_NAME = 'CTE_teste'

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()
# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'CTE TEXT,'
    'Peso REAL'
    'Dt_Emissao Date'
    'uf_origem TEXT'
    'uf_destino TEXT'
    'CO_Destino TEXT'
    ')'
)


with connection.cursor() as cursor:
    sql = (
        f'INSERT INTO {TABLE_NAME} '
        '(CTE, Peso, Dt_Emissao,uf_origem, uf_destino, CO_Destino ) '
        'VALUES '
        '(%(CTE)s, %(Peso)s, %(Dt_Emissao)s, %(uf_origem)s, %(uf_destino)s, %(CO_Destino)s) '
    )

    data3 = (
        {"name": "Cordeiro", "age": 45, },
        {"name": "Clodoaldo", "age": 48, },
        {"name": "Cintia", "age": 29, },
    )

    result = cursor.executemany(sql, BD)  # type: ignore
# cursor.execute  #Para um unico valor
# cursor.executemany  #Para muitos valores

cursor.executemany(sql,
                   [
                       ['Fabio Alves Cordeiro', 102],
                       ['Luciene Almeida da Silva', 97],
                       ['Lucas da Silva Cordeiro', 25],

                   ])


connection.commit()
print(sql)

cursor.close()
connection.close()

# '''

print('Fim')

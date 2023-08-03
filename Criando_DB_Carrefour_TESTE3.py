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
                 sep='|', nrows=5, usecols=[1, 2], low_memory=False)
# pd.options.display.max_rows = 5
BD.describe()
BD.info(memory_usage=dict)
print(BD)

TABLE_NAME = 'CTE_teste_3'

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
    f'CREATE TABLE IF NOT EXISTS CTE_teste_3'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'CTE TEXT,'
    'Peso REAL'
    ')'
)


connection.commit()
cursor.close()
connection.close()


print('Fim')

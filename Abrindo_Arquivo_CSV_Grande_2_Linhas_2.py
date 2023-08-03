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

# abrindo o arquivo CSV e mostrando 5 linhas.
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


print(f'{"Imprimindo o For 1 linha":^60}')
for linha in range(len(BD)):
    print(linha)
    base.append(linha)
    print(f'linha:{linha}')
BD.to_excel('BD.xlsx')
# base.to_excel('base.xlsx')
print(f'{"Imprimindo a base inteira":^60}')
print(base)
print('Fim leitura')
print(f'{"Imprimindo o BD":^60}')
print(BD)
print(f'{"Imprimindo o For 2 com index":^60}')
for index, row in BD.iterrows():
    print(f'Index: {index} linha {row}')
    print(row)
    base1.append(row)
    print(f'row:{row}')
    print(row)
# base1.to_excel('base1.xlsx')
print(f'{"Imprimindo a base1 inteira":^60}')
print(base1)
print(60*'-')
print(f'{"Imprimindo o For com Intertuples()":^60}')
for row in BD.itertuples():
    print(f'linha {row}')
    print(row)
    base2.append(row)
print(60*'-')
print(f'{"Imprimindo a base2 inteira":^60}')
print(base2)
# base2.to_excel('base2.xlsx')


with connection.cursor() as cursor:
    sql = (
        f'INSERT INTO {TABLE_NAME} '
        '(CTE, Peso, Dt_Emissao Date, uf_destino, uf_origem, Cidade_Destino , CO_Origem, CO_Destino, CEP, Tarifa, Opcao_Entrega, Valor_Dec, ad_valorem, Coleta, Embalagem, Entrega, icms, TX_entrega_Central, TX_entrega_Destino, TX_entrega_Origem, FOB, Frete, Gris, Interior, Reversa, TDE, Faturamento, Conta_Corrente, CNPJ_tomador, CNPJ_remetente, Produto, Razao_Social)'
        'VALUES'
        '(%(CTE)s, %(Peso)s, %(Dt_Emissao Date)s, %(uf_destino)s, %(uf_origem)s, %(Cidade_Destino)s, %(CO_Origem)s, %(CO_Destino)s, %(CEP)s, %(Tarifa)s, %(Opcao_Entrega)s, %(Valor_Dec)s, %(ad_valorem)s, %(Coleta)s, %(Embalagem)s, %(Entrega)s, %(icms)s, %(TX_entrega_Central)s, %(TX_entrega_Destino)s, %(TX_entrega_Origem)s, %(FOB)s, %(Frete)s, %(Gris)s, %(Interior)s, %(Reversa)s, %(TDE)s, %(Faturamento)s, %(Conta_Corrente)s, %(CNPJ_tomador)s, %(CNPJ_remetente)s, %(Produto)s, %(Razao_Social)s)'
    )

    result = cursor.executemany(sql, BD)  # type: ignore
'''


with open('CTE.csv', 'r') as file:
    records = 0
    for row in file:
        cursor.execute(
            "INSERT INTO {TABLE_NAME} VALUES (?,?,?,?,?  )", row.split("|"))
        connection.commit()
        records += 1
connection.close()

print('\n [] Records Transfer Completed'.format(records))
# cursor.execute  #Para um unico valor
# cursor.executemany  #Para muitos valores
'''
cursor.executemany(sql,
                   [
                       ['Fabio Alves Cordeiro', 102],
                       ['Luciene Almeida da Silva', 97],
                       ['Lucas da Silva Cordeiro', 25],

                   ])

'''
connection.commit()
print(sql)
cursor.close()
connection.close()

# '''

print('Fim')

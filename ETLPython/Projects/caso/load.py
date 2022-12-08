from transform import tablon, today

import pandas as pd
import numpy as np
import pyodbc

# TODO:
# - 3.1 - Validate the operation in markets during the day of the flow. Discard the flow records in case it has not operated on the day
# - 3.2 - Create table if not exist
# - 3.3 - Check if the record exists. If it exists we discard it
# - 3.4 - Insertion of records in the table

num_rows_tablon = len(tablon.index)

# 3.1
if num_rows_tablon != 1:
    print("Data conflicts. not run on NASDAQ today")
    # return

# 3.2
name_cols_sql = [ '[' + col + ']' for col in tablon.columns ]

sql_create_valor_btc = """
        IF NOT EXISTS (SELECT name FROM sys.tables WHERE name = 'btcvalores')
            CREATE TABLE btcvalores (
                [fecha] DATE PRIMARY KEY,
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} VARCHAR,
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} VARCHAR,
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} VARCHAR,
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} VARCHAR,
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} VARCHAR,
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} DECIMAL (20, 2),
                {} VARCHAR,
                {} DECIMAL (20, 2)
        )""".format(*name_cols_sql)

server = 'tcp:ud-caso-btc.database.windows.net'
database = 'caso_nasdaq_btc'
username = 'admin_ud'
password = 'edefs.01'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';')
cursor = cnxn.cursor()
cursor.execute(sql_create_valor_btc)
cnxn.commit()

print(sql_create_valor_btc)
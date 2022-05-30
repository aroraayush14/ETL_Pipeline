#importing packages
from sqlalhemy import create_engine
import pyodbc
import pandas as pd 
import os
#
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']

driver = "{SQL Server Native Client 11.0}"
server = 'localhost'
database = 'AdventureWorksDW2019'

def extract():
    try:
        src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS'   +  ';DATABASE=' + database + ';PGUID=' + uid + ';PWD=' + pwd)
        src_cursor = src_conn.cursor()
        src_cursor.execute(""" select  t.name as table_name
        from sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductSubcategory','DimProductCategory','DimSalesTerritory','FactInternetSales') """)
        src_tables = src_cursor.fetchall()
        for tbl in src_tables:
            df = pd.read_sql_query(f'select * FROM {tbl[0]}', src_conn)
            load(df, tbl[0])
    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        src_conn.close()

#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/AdventureWorks')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
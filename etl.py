from sqlalhemy import create_engine
import pyodbc
import pandas as pd 
import os

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
            df = pd.read_sql_query
# Data Extraction and Loading Script

This Python script connects to a SQL Server database, extracts specific tables' data, and loads it into a PostgreSQL database.

## Prerequisites

### Packages
- `sqlalchemy`: SQL toolkit and Object-Relational Mapping (ORM) library
- `pyodbc`: Python DB API 2 module for ODBC
- `pandas`: Data manipulation and analysis library

Make sure to have these packages installed in your Python environment.

## Configuration

Before running the script, ensure the following:

### Environment Variables
- Set the environment variables `PGPASS` and `PGUID` with appropriate credentials.

## Usage

### Running the Script
- Modify the `server`, `database`, and specific table names in the `extract` function to suit your SQL Server setup and desired tables.
- Ensure your PostgreSQL database configuration (server, port, credentials) is correct in the `load` function.
- Execute the script.

## Functions

### `extract()`
- Establishes a connection to a SQL Server database (`AdventureWorksDW2019` in this case).
- Fetches specific tables (`DimProduct`, `DimProductSubcategory`, `DimProductCategory`, `DimSalesTerritory`, `FactInternetSales`) from the SQL Server database.
- Reads each table's data into a Pandas DataFrame and calls the `load` function.

### `load(df, tbl)`
- Loads the DataFrame into a PostgreSQL database (`AdventureWorks`) using SQLAlchemy's `create_engine` method.
- Creates staging tables (`stg_{table_name}`) in the PostgreSQL database and replaces existing data if it already exists.

## Error Handling

The script contains error handling mechanisms to catch exceptions during the extraction and loading processes. Ensure to check the console output for any error messages in case of failure.

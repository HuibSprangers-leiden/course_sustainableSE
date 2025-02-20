import sqlite3
import pandas as pd

db_path = 'olist.sqlite\olist.sqlite'
db_connection = sqlite3.connect(db_path)

def view_table(table, limit):
    query = f"""
        SELECT *
        FROM {table}
        LIMIT {limit}
    """
    return pd.read_sql_query(query, db_connection)
print(view_table('products', 5))
import sqlite3
import pandas as pd

# Put database file: 'olist.sqlite' in same folder as this file. 
# Download database file: https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database?resource=download
db_path = 'convert_sqlite_to_sql/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# Generate requests:
def view_table(table, limit):
    query = f"""
        SELECT *
        FROM {table}
        LIMIT {limit}
    """
    return pd.read_sql_query(query, db_connection)

# Print results of sql request:
print(view_table('products', 5))
import sqlite3
from pyEnergiBridge.api import EnergiBridgeRunner

conn = sqlite3.connect("./convert_sqlite_to_sql/olist.sqlite")
cursor = conn.cursor()

runner = EnergiBridgeRunner()
runner.start(results_file="results_sqlite.csv")

# Go over every table and execute SELECT * on each table 
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

conn.close()

energy, duration = runner.stop()
print(f"Energy consumption (J): {energy}; Execution time (s): {duration}")

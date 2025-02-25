from pyEnergiBridge.api import EnergiBridgeRunner
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "user_CS4575",
    "password": "password_CS4575",
    "database": "olist_e-commerce"
}

runner = EnergiBridgeRunner()
runner.start(results_file="results_mysql.csv")

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Go over every table and execute SELECT * on each table 
try:
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT * FROM `{table_name}`;")
        cursor.fetchall()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn.is_connected():
        conn.close()

energy, duration = runner.stop()
print(f"Energy consumption (J): {energy}; Execution time (s): {duration}")

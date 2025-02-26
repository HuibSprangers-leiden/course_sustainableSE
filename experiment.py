# gets run by controller.py for measurements

import sqlite3
import sys
import mysql.connector

from constants import (
    DB_FILE,
    MYSQL_DB,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_USER,
    NUM_QUERIES,
    TABLES,
)

db = sys.argv[1]

try:
    if db == "mysql":
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
        )
        cursor = connection.cursor()
    elif db == "sqlite":
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
    else:
        raise ValueError("Invalid database")

    for _ in range(NUM_QUERIES):
        for table in TABLES:
            query = f"SELECT * FROM `{table}`;"
            cursor.execute(query)
            values = cursor.fetchall()
            # print(f"{table}: {len(  values)} rows")
    cursor.close()
    connection.close()
except Exception as err:
    print(f"Error: {err}")

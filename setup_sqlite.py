import sqlite3
import os
import csv

from constants import DATA_FOLDER, DB_FILE, TABLES



def create_db():
    with open("create_sqlite_db.sql", "r") as file:
        sql_script = file.read()

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.executescript(sql_script)

    connection.commit()
    cursor.close()
    connection.close()

    print("SQLite database and tables created successfully.")


def import_data():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    for table in TABLES:
        path = f"{DATA_FOLDER}/{table}.csv"

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                columns = next(reader)  # Read header
                placeholders = ", ".join(["?" for _ in columns])
                query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"

                try:
                    cursor.executemany(query, reader)
                    connection.commit()
                    print(f"Successfully imported {table}")
                except sqlite3.Error as err:
                    print(f"Error importing {table}: {err}")
        else:
            print(f"File not found: {path}")

    cursor.close()
    connection.close()
    print("CSV data import completed.")


def get_table_counts():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    counts = {}
    for table in TABLES:
        query = f"SELECT COUNT(*) FROM {table};"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        # print(f"{table}: {count} rows")
        counts[table] = count

    cursor.close()
    connection.close()

    return counts


if __name__ == "__main__":
    create_db()
    import_data()
    get_table_counts()

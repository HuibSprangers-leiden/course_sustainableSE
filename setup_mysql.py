import mysql.connector
import os

from constants import (
    DATA_FOLDER,
    MYSQL_DB,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_USER,
    TABLES,
)


def create_db():
    with open("create_mysql_db.sql", "r") as file:
        sql_script = file.read()

    connection = mysql.connector.connect(
        host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD
    )
    cursor = connection.cursor()

    for statement in sql_script.split(";"):
        if statement.strip():  # skip empty lines
            try:
                print(f"{statement}")
                cursor.execute(statement)
            except mysql.connector.Error as err:
                print(f"{err}")

    print("Database and tables created successfully.")


def import_data():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        allow_local_infile=True,
    )
    cursor = connection.cursor()

    for table in TABLES:
        path = f"{DATA_FOLDER}/{table}.csv"
        print(path)

        if os.path.exists(path):
            query = f"""
            LOAD DATA LOCAL INFILE '{path}'
            INTO TABLE {table}
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
            """

            try:
                cursor.execute(query)
                connection.commit()
                print(f"Successfully imported {table}")
            except mysql.connector.Error as err:
                print(f"Error importing {table}: {err}")
        else:
            print(f"File not found: {path}")

    cursor.close()
    connection.close()
    print("CSV data import completed.")


def get_table_counts(connection):
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

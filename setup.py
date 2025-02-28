# This file sets up the databases and imports data. It is important to run this file before running the experiments

from setup_mysql import (
    create_db as create_mysql_db,
    import_data as import_mysql_data,
    get_table_counts as get_mysql_table_counts,
)

from setup_sqlite import (
    create_db as create_sqlite_db,
    import_data as import_sqlite_data,
    get_table_counts as get_sqlite_table_counts,
)


def setup_mysql():
    create_mysql_db()
    import_mysql_data()
    print("MySQL setup completed.")
    return get_mysql_table_counts()


def setup_sqlite():
    create_sqlite_db()
    import_sqlite_data()
    print("SQLite setup completed.")
    return get_sqlite_table_counts()


if __name__ == "__main__":
    mysql_counts = setup_mysql()
    sqlite_counts = setup_sqlite()

    for table in mysql_counts:
        print(
            f"{table}: MySQL - {mysql_counts[table]}, SQLite - {sqlite_counts[table]}"
        )

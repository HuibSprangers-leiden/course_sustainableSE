import sqlite3

# Define MySQL specific data type mapping
TYPE_MAPPING = {
    "INTEGER": "INT",
    "TEXT": "VARCHAR(255)",
    "REAL": "FLOAT",
    "BLOB": "LONGBLOB",
    "NUMERIC": "DECIMAL(10,2)"
}

def convert_sqlite_to_mysql(sqlite_file, output_sql_file, max_size):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    
    with open(output_sql_file, "w", encoding="utf-8") as f:
        f.write("DROP DATABASE IF EXISTS `olist_e-commerce`;\nCREATE DATABASE `olist_e-commerce`;\nUSE `olist_e-commerce`;\n\n")
        # f.write("SET foreign_key_checks = 0;\n")

        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table_name in tables:
            print(table_name)
            table_name = table_name[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            create_stmt = f"CREATE TABLE {table_name} (\n"
            col_definitions = []
            
            for col in columns:
                col_name, col_type, not_null, default, pk = col[1], col[2], col[3], col[4], col[5]
                mysql_col_type = TYPE_MAPPING.get(col_type.upper(), "TEXT")
                col_def = f"{col_name} {mysql_col_type}"
                if pk:
                    col_def += " PRIMARY KEY"
                elif not_null:
                    col_def += " NOT NULL"
                if default is not None:
                    col_def += f" DEFAULT '{default}'"
                col_definitions.append(col_def)
                
            create_stmt += ",\n".join(col_definitions) + "\n);\n\n"
            f.write(create_stmt)
            
            # Extract and convert data
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            if rows:
                col_names = [desc[0] for desc in cursor.description]
                f.write(f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES\n")
                for i, row in enumerate(rows):
                    if i <= max_size :
                        values_list = []
                        for val in row:
                            if val is not None:
                                if isinstance(val, bytes):  # Handle BLOB data
                                    values_list.append(f"X\'{val.hex()}\'")  # Convert bytes to hex for MySQL
                                else:
                                    fixed_val = str(val).replace("\'", "\'\'")
                                    values_list.append(f"\'{fixed_val}\'")
                            else:
                                values_list.append("NULL")
                        values = ", ".join(values_list)
                        if i == max_size or i == len(rows) - 1:
                            f.write(f"({values});\n")
                        else:
                            f.write(f"({values}),\n")
        
        # f.write("SET foreign_key_checks = 1;\n")
        
    conn.close()
    print(f"Conversion complete. SQL dump saved to {output_sql_file}")

# Run conversion
max_size = 100
convert_sqlite_to_mysql('convert_sqlite_to_sql/olist.sqlite', f"convert_sqlite_to_sql/olist_mysql_{max_size}_entries.sql", max_size)

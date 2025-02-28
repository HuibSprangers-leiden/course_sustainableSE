# This file contains the constants used in the experiments

MYSQL_USER = "mysql"
MYSQL_PASSWORD = "mysql"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "olist"

DB_FILE = "db/olist.db"  # for sqlite


DATA_FOLDER = "C:/Users/simon/Documents/Code/suts/data"  # folder containing CSV files

TABLES = [
    "customers",
    "geolocation",
    # "order_items",
    # "order_payments",
    # "order_reviews",
    "orders",
    "products",
    "sellers",
    # "product_category_name_translation",
]  # removed buggy tables

NUM_EXPERIMENTS = 30  # number of experiments to run per option
NUM_QUERIES = 1  # number of queries per experiment
REST_TIME = 20  # seconds to rest between experiments

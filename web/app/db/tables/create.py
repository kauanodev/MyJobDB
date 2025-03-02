from app.db.connection import db_connection
from psycopg2.extensions import cursor as Cursor
import os


def create_tables():
    query = get_query()
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    print(query)
    cursor.execute(query)
    connection.commit()


def get_query():
    create_file_path = os.path.abspath(__file__)
    db_dir = os.path.dirname(create_file_path)
    app_dir = os.path.dirname(db_dir)
    web_dir = os.path.dirname(app_dir)
    root_dir = os.path.dirname(web_dir)
    tables_dir = os.path.join(os.path.dirname(root_dir), "tables")
    all_sql_files = os.listdir(tables_dir)
    sorted_sql_files = sorted(
        all_sql_files, key=lambda x: int(x.split('_')[0]))

    the_sql = ""

    for sql_file_name in sorted_sql_files:
        sql_file_path = os.path.join(tables_dir, sql_file_name)
        sql_file = open(sql_file_path, "r")
        sql = sql_file.read()
        the_sql += f"--- {sql_file_name}\n{sql}\n"
        sql_file.close()

    return the_sql

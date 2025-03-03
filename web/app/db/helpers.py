import os
from app.settings import APP_ROOT
from app.db.tables.index import Table


def get_query_file_path(table: Table):
    app_dir = APP_ROOT
    web_dir = os.path.dirname(app_dir)
    root_dir = os.path.dirname(web_dir)
    queries_dir = os.path.join(root_dir, "queries")
    all_sql_files = os.listdir(queries_dir)
    for sql_file_name in all_sql_files:
        file_index = int(sql_file_name.split('_')[0])
        if file_index == table.value:
            return os.path.join(queries_dir, sql_file_name)


def get_query_from_file(file_path: str, query_type: (str, str)):
    start_read = False
    file = open(file_path)
    query = ""
    for line in file.readlines():
        is_a_comment = line.startswith("--")
        removed_comment = line.replace("--", "").strip()
        if removed_comment == query_type[1]:
            break
        if is_a_comment and removed_comment == query_type[0]:
            start_read = True
            continue
        if start_read:
            query += line
    return query

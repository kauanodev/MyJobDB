import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
tables_dir = os.path.join(os.path.dirname(script_dir), "tables")
all_sql_files = os.listdir(tables_dir)
sorted_sql_files = sorted(all_sql_files, key=lambda x: int(x.split('_')[0]))

the_sql = ""

for sql_file_name in sorted_sql_files:
    sql_file_path = os.path.join(tables_dir, sql_file_name)
    sql_file = open(sql_file_path, "r")
    sql = sql_file.read()
    the_sql += f"--- {sql_file_name}\n{sql}\n"
    sql_file.close()

print("COPY THE SQL:\n")
print(the_sql, end="")

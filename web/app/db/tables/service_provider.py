from app.db import helpers
from app.db.connection import db_connection
from app.db.tables.index import Table, QueryType
from psycopg2.extensions import cursor as Cursor


def select_many(data: tuple):
    file_path = helpers.get_query_file_path(Table.SERVICE_PROVIDER)
    select_query = helpers.get_query_from_file(
        file_path,
        QueryType.SELECT_MANY.value
    )
    print(select_query, data)
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    cursor.execute(select_query, (data))
    tuples = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    results = [dict(zip(colnames, row)) for row in tuples]
    connection.commit()
    return results


def select_one(id: int, data: tuple):
    file_path = helpers.get_query_file_path(Table.SERVICE_PROVIDER)
    select_query = helpers.get_query_from_file(
        file_path,
        QueryType.SELECT.value
    )
    print(select_query, id, data)
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    cursor.execute(select_query, (id,))
    tuples = cursor.fetchone()
    colnames = [desc[0] for desc in cursor.description]
    results = dict(zip(colnames, tuples))
    connection.commit()
    return results


def insert(data: tuple):
    file_path = helpers.get_query_file_path(Table.SERVICE_PROVIDER)
    insert_query = helpers.get_query_from_file(
        file_path,
        QueryType.INSERT.value
    )
    print(insert_query, data)
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    cursor.execute(insert_query, data)
    connection.commit()


def update(id: int, data: tuple):
    file_path = helpers.get_query_file_path(Table.SERVICE_PROVIDER)
    update_query = helpers.get_query_from_file(
        file_path,
        QueryType.UPDATE.value
    )
    print(update_query, id, data)
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    cursor.execute(update_query, (*data, id))
    connection.commit()


def delete(id: int):
    file_path = helpers.get_query_file_path(Table.SERVICE_PROVIDER)
    delete_query = helpers.get_query_from_file(
        file_path,
        QueryType.DELETE.value
    )
    print(delete_query, id)
    connection = db_connection()
    cursor: Cursor = connection.cursor()
    cursor.execute(delete_query, (id,))
    connection.commit()

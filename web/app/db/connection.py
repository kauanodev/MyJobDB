import psycopg2
from psycopg2.extensions import connection as Connection
from typing import Callable
from app.settings import (
    DATABASE_NAME,
    DATABASE_HOST,
    DATABASE_USERNAME,
    DATABASE_PASSWORD
)


def get_db_connection() -> Callable[[], Connection]:
    connection: Connection = None

    def create_connection() -> Connection:
        nonlocal connection
        if connection is None:
            connection = psycopg2.connect(
                dbname=DATABASE_NAME,
                user=DATABASE_USERNAME,
                password=DATABASE_PASSWORD,
                host=DATABASE_HOST
            )
        return connection

    return create_connection


db_connection = get_db_connection()

from os import environ
import psycopg
from psycopg.sql import SQL, Composed
import ramda as R
from typing import TypedDict
import pandas as pd


class DBCredentials(TypedDict):
    user: str
    password: str
    database: str
    host: str
    port: int

class Connection(psycopg.Connection):
    def __deepcopy__(self, memo):
        return self


def read_db_credentials_from_env() -> DBCredentials:
    return {
        "user": environ.get("POSTGRES_USER"),
        "password": environ.get("POSTGRES_PASSWORD"),
        "dbname": environ.get("POSTGRES_DB"),
        "host": environ.get("POSTGRES_HOST"),
        "port": int(environ.get("POSTGRES_PORT"))
    }


def connect_to_db(credentials: DBCredentials) -> Connection:
    return psycopg.connect(**credentials)


def teardown_db_connection(connection: Connection) -> Connection:
    connection.commit()
    connection.close()
    return connection


def query_df(query: str | SQL | Composed) -> pd.DataFrame:
    try:
        conn = create_db_connection()
        return pd.read_sql(query, conn)
    finally:
        teardown_db_connection(conn)


create_db_connection = R.pipe(read_db_credentials_from_env, connect_to_db)
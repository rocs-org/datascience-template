import ramda as R

from os import environ
from typing import TypedDict
from dask_clickhouse import read_clickhouse
from dask.dataframe import DataFrame

class DBCredentials(TypedDict):
    user: str
    password: str
    database: str
    host: str
    port: int
    
def read_clickhouse_credentials_from_env() -> DBCredentials:
    return {
        "user": environ.get("CLICKHOUSE_USER"),
        "password": environ.get("CLICKHOUSE_PASSWORD"),
        "database": environ.get("CLICKHOUSE_DB"),
        "host": environ.get("CLICKHOUSE_HOST"),
        "port": int(environ.get("CLICKHOUSE_PORT")),
    }

def query_dd(query: str) -> DataFrame:
    """
    Read query from clickhouse and return results as dask dataframe.
    
    Initialize a dask cluster before using this function via
    
    from dask_gateway import GatewayCluster
    cluster = GatewayCluster()
    """
    credentials = read_clickhouse_credentials_from_env()
    return read_clickhouse(
            query=query,
            connection_kwargs=credentials
    )
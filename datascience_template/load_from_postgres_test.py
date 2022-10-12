from datascience_template import create_db_connection, teardown_db_connection, query_df
import pandas as pd

def test_create_db_connection_is_open_and_can_be_closed():
    connection = create_db_connection()
    assert connection.closed == 0
    
    teardown_db_connection(connection)
    
    assert connection.closed == 1
    
    
def test_can_execute_sql_on_connection():
    conn = create_db_connection()
    df = pd.read_sql("select * from datenspende_derivatives.homogenized_features LIMIT 10;", conn)
    
    assert len(df) == 10
    assert 'questionnaire_session' in df.columns
    
    teardown_db_connection(conn)
    
    
def test_query_df_returns_df():
    df = query_df("select * from datenspende_derivatives.homogenized_features LIMIT 10;")
        
    assert len(df) == 10
    assert 'questionnaire_session' in df.columns
    
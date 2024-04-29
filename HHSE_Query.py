import sqlite3
import pandas as pd

def query_students(conn, field, value):
    """
    Query students from the database based on the provided field and value.

    Parameters:
    - conn: SQLite connection object.
    - field: The field to query by.
    - value: The value to search for.

    Returns:
    - A pandas DataFrame containing the query results.
    """
    query = f'''SELECT * FROM students WHERE {field} = ?'''
    df = pd.read_sql_query(query, conn, params=(value,))
    return df
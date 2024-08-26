from typing import Any, Optional

import psycopg2
from settings import Settings


class ConnectionManager:
    _instance = None
    _connection = None
    _connection_str = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionManager, cls).__new__(cls)
            cls._connection_str = Settings().DB_CONNECTION_STRING
            # Connect to PostgreSQL database
            cls._connection = psycopg2.connect(cls._connection_str, connect_timeout=0)

        return cls._instance

    @classmethod
    def get_connection(cls):
        if cls._connection is None and cls._connection_str is not None:
            cls._connection = psycopg2.connect(cls._connection_str, connect_timeout=0)
        elif cls._connection is None and cls._connection_str is None:
            raise Exception("Call ConnectionManager() first")

        return cls._connection

    @classmethod
    def reset_connection(cls):
        try:
            cls._connection.close()
            cls._connection = psycopg2.connect(cls._connection_str, connect_timeout=0)
        except Exception as e:
            print(f"Reset connection exception: {e}")
            cls._connection = psycopg2.connect(cls._connection_str, connect_timeout=0)

        return cls._connection


def execute_query(
    query: str = None,
    op: str = "SELECT",
) -> Optional[list[tuple]]:
    """
    Execute a plain SQL query

    Args:
        - SQL query

    Return:
        - data if op="SELECT" else None
    """
    if query is None:
        raise Exception("Please provide query")

    # Get the persistent connection
    try:
        conn = ConnectionManager.get_connection()
        cur = conn.cursor()
    except Exception as e:
        print(f"Reset connection because of: {e}")
        conn = ConnectionManager.reset_connection()
        cur = conn.cursor()

    # Execute + fetch result
    try:
        cur.execute(query)
        if op == "SELECT":
            data = cur.fetchall()
        else:
            data = None
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Cannot run query. Error: {e}")

    # Close cursor (not the connection)
    cur.close()

    return data


def deduplicate_list(
    text_list: list[Any],
) -> list[Any]:
    """
    Deduplicate elements in the list but keep the order

    Args:
        - a list

    Return:
        - list without duplicated elements
    """
    seen = set()
    result = []
    for text in text_list:
        if text not in seen:
            seen.add(text)
            result.append(text)

    return result


ConnectionManager()

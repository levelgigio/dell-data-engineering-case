import psycopg2


def connect2db():
    # Establishing the connection
    conn = psycopg2.connect(
        database="test",
        user="dellPostgresUser",
        password="dellPostgresPW",
        host="127.0.0.1",
        port="5455",
    )
    return conn

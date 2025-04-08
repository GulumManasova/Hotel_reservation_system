import sqlite3

def get_db_connection():
    conn = sqlite3.connect('hoteldatabase.sqlite')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

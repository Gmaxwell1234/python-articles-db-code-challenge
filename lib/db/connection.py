import sqlite3

CONN = sqlite3.connect('db/magazine.db')
CURSOR = CONN.cursor()

def get_connection():
    return CONN

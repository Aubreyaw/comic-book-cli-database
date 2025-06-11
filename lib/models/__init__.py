import sqlite3

CONN = sqlite3.connect('comics.db')
CURSOR = CONN.cursor()

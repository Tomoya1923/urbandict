import sqlite3

DATABASE = 'database.db'

def create_dictionary_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS dicts (word, description, user_id)")
    con.close()
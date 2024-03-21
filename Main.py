print("Hello Word")

import sqlite3

conn = sqlite3.connect('BancoDeDados.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);
'''

cursor.execute(create_table_query)

conn.commit()

conn.close()
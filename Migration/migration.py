import sqlite3

def init_db():
    conn = sqlite3.connect('Banco/BancoDeDados.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ong (
        id INTEGER PRIMARY KEY,
        externalUuid TEXT NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        razaosocial TEXT NOT NULL,
        password TEXT NOT NULL,
        CNPJ TEXT NOT NULL,
        is_deleted BOOLEAN DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Voluntario (
        id INTEGER PRIMARY KEY,
        externalUuid TEXT NOT NULL,
        nome TEXT NOT NULL,
        CPF TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        is_deleted BOOLEAN DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Evento (
        id INTEGER PRIMARY KEY,
        externalUuid TEXT NOT NULL,
        tipo TEXT NOT NULL,
        nome TEXT NOT NULL,
        local TEXT NOT NULL,
        data TIMESTAMP,
        publico TEXT NOT NULL,
        marketing TEXT NOT NULL,
        fornecedores TEXT NOT NULL,
        doacoes TEXT NOT NULL,
        nomeOng TEXT NOT NULL,
        is_deleted BOOLEAN DEFAULT 0,
        FOREIGN KEY (nomeOng) REFERENCES Ong(nome)
    )
    ''')

    conn.commit()
    conn.close()
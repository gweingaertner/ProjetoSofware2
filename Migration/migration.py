import sqlite3

conn = sqlite3.connect('../Banco/BancoDeDados.db')

cursor = conn.cursor()

usuario = '''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY,
    externalUuid TEXT NOT NULL,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    is_deleted  BOOLEAN DEFAULT 0,
);
'''

Ong = '''
CREATE TABLE IF NOT EXISTS Ong (
    id INTEGER PRIMARY KEY,
    externalUuid TEXT NOT NULL,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    is_deleted  BOOLEAN DEFAULT 0,
);
'''

Evento = '''
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
    doaçoes TEXT NOT NULL,
    nomeOng TEXT NOT NULL,
    is_deleted  BOOLEAN DEFAULT 0,
    FOREIGN KEY (nomeOng) REFERENCES Ong(nome)
    )
'''

cursor.execute(usuario)
cursor.execute(Ong)
cursor.execute(Evento)
conn.commit()

conn.close()

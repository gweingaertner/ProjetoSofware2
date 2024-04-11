import sqlite3
import uuid

def conectar_banco():
    conn = sqlite3.connect('Banco/BancoDeDados.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_ong(nome, email, razaosocial, password, CNPJ):
    conn, cursor = conectar_banco()
    cursor.execute('''
        INSERT INTO Ong (externalUuid, nome, email, razaosocial, password, CNPJ)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (str(uuid.uuid4()), nome, email, razaosocial, password, CNPJ))
    conn.commit()
    conn.close()

def buscar_ongs():
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM Ong WHERE is_deleted = 0')
    ongs = cursor.fetchall()
    conn.close()
    return ongs

def buscar_ong_por_id(externalUuid):
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM Ong WHERE externalUuid = ? AND is_deleted = 0', (externalUuid,))
    ong = cursor.fetchone()
    conn.close()
    return ong

def atualizar_ong(externalUuid, nome, email, razaosocial, password, CNPJ):
    conn, cursor = conectar_banco()
    cursor.execute('''
        UPDATE Ong
        SET nome = ?, email = ?, razaosocial = ?, password = ?, CNPJ = ?
        WHERE externalUuid = ?
    ''', (nome, email, razaosocial, password, CNPJ, externalUuid))
    conn.commit()
    conn.close()

def deletar_ong(externalUuid):
    conn, cursor = conectar_banco()
    cursor.execute('UPDATE Ong SET is_deleted = 1 WHERE externalUuid = ?', (externalUuid,))
    conn.commit()
    conn.close()
import sqlite3
import uuid

def conectar_banco():
    conn = sqlite3.connect('Banco/BancoDeDados.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_evento(tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nomeOng):
    conn, cursor = conectar_banco()
    cursor.execute('''
        INSERT INTO Evento (externalUuid, tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nomeOng)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (str(uuid.uuid4()), tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nomeOng))
    conn.commit()
    conn.close()

def buscar_eventos():
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM Evento WHERE is_deleted = 0')
    eventos = cursor.fetchall()
    conn.close()
    return eventos

def buscar_evento_por_id(externalUuid):
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM Evento WHERE externalUuid = ? AND is_deleted = 0', (externalUuid,))
    evento = cursor.fetchone()
    conn.close()
    return evento

def atualizar_evento(externalUuid, tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nomeOng):
    conn, cursor = conectar_banco()
    cursor.execute('''
        UPDATE Evento
        SET tipo = ?, nome = ?, local = ?, data = ?, publico = ?, marketing = ?,
        fornecedores = ?, doacoes = ?, nomeOng = ?
        WHERE externalUuid = ?
    ''', (tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nomeOng, externalUuid))
    conn.commit()
    conn.close()

def deletar_evento(externalUuid):
    conn, cursor = conectar_banco()
    cursor.execute('UPDATE Evento SET is_deleted = 1 WHERE externalUuid = ?', (externalUuid,))
    conn.commit()
    conn.close()

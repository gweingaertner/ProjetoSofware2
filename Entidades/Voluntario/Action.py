import sqlite3
import uuid

def conectar_banco():
    conn = sqlite3.connect('Banco/BancoDeDados.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_voluntario(nome, CPF, email, password):
    conn, cursor = conectar_banco()
    cursor.execute('''
        INSERT INTO Voluntario (externalUuid, nome, CPF, email, password)
        VALUES (?, ?, ?, ?, ?)
    ''', (str(uuid.uuid4()), nome, CPF, email, password))
    conn.commit()
    conn.close()

def buscar_voluntarios():
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM Voluntario WHERE is_deleted = 0')
    voluntarios = cursor.fetchall()
    conn.close()
    return voluntarios

def buscar_voluntario_por_id(externalUuid):
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM Voluntario WHERE externalUuid = ? AND is_deleted = 0', (externalUuid,))
    voluntario = cursor.fetchone()
    conn.close()
    return voluntario

def atualizar_voluntario(externalUuid, nome, CPF, email, password):
    conn, cursor = conectar_banco()
    cursor.execute('''
        UPDATE Voluntario
        SET nome = ?, CPF = ?, email = ?, password = ?
        WHERE externalUuid = ?
    ''', (nome, CPF, email, password, externalUuid))
    conn.commit()
    conn.close()

def deletar_voluntario(externalUuid):
    conn, cursor = conectar_banco()
    cursor.execute('UPDATE Voluntario SET is_deleted = 1 WHERE externalUuid = ?', (externalUuid,))
    conn.commit()
    conn.close()
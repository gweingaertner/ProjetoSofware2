import sqlite3
import uuid

def connect_db():
    conn = sqlite3.connect('../Banco/BancoDeDados.db')
    return conn

def create_user(external_uuid, nome, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO User (externalUuid, nome, email, password) VALUES (?, ?, ?, ?)', (external_uuid, nome, email, password))
    conn.commit()
    conn.close()

def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user_nome(user_id, new_nome):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE User SET nome=? WHERE id=?', (new_nome, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM User WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

def create_ong(external_uuid, nome, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Ong (externalUuid, nome, email, password) VALUES (?, ?, ?, ?)', (external_uuid, nome, email, password))
    conn.commit()
    conn.close()

def get_all_ongs():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ong')
    ongs = cursor.fetchall()
    conn.close()
    return ongs

# Funções para a tabela de Eventos (Evento)
def create_evento(external_uuid, tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nome_ong):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Evento (externalUuid, tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nomeOng) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (external_uuid, tipo, nome, local, data, publico, marketing, fornecedores, doacoes, nome_ong))
    conn.commit()
    conn.close()

def get_all_eventos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Evento')
    eventos = cursor.fetchall()
    conn.close()
    return eventos


create_user(str(uuid.uuid4()), 'Nome do Usuário', 'email@example.com', 'password123')


print("Usuários:")
print(get_all_users())


update_user_nome(1, 'Novo Nome')

delete_user(1)

create_ong(str(uuid.uuid4()), 'Nome da ONG', 'ong@example.com', 'password123')

print("\nONGs:")
print(get_all_ongs())


create_evento(str(uuid.uuid4()), 'Tipo do Evento', 'Nome do Evento', 'Local do Evento', '2024-03-21', 'Público-alvo', 'Estratégia de Marketing', 'Fornecedores', 'Doações', 'Nome da ONG')


print("\nEventos:")
print(get_all_eventos())
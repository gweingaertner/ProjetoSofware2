from flask import Blueprint, render_template, request, redirect, url_for
from flask import Blueprint, jsonify, request
import sqlite3

login_routes = Blueprint('login_routes', __name__)

# Dados de exemplo para simular um banco de dados de usuários
usuarios = {
    "usuario1@example.com": "senha1",
    "usuario2@example.com": "senha2",
    "usuario3@example.com": "senha3"
}

def verificar_credenciais(email, senha):
    conn = sqlite3.connect('Banco/BancoDeDados.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Voluntario
        WHERE email = ? AND password = ?
    ''', (email, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario


@login_routes.route('/')
def index():
    return render_template('index.html')


# Rota para processar o formulário de login
@login_routes.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    usuario = verificar_credenciais(email, senha)
    if usuario:
        # Login bem-sucedido, redireciona para a página de perfil
        return redirect(url_for('login_routes.perfil', email=email))
    else:
        # Login falhou, redireciona de volta para a página de login
        return redirect(url_for('login_routes.index'))


@login_routes.route('/perfil/<email>')
def perfil(email):
    return f"<h1>Bem-vindo, {email}!</h1>"

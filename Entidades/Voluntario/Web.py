from flask import Blueprint, jsonify, request
import sqlite3
from Entidades.Voluntario.Action import criar_voluntario, buscar_voluntarios, buscar_voluntario_por_id, atualizar_voluntario, deletar_voluntario

voluntario_routes = Blueprint('voluntario_routes', __name__)

@voluntario_routes.route('/voluntarios', methods=['POST'])
def criar_voluntario_route():
    data = request.json
    criar_voluntario(data['nome'], data['CPF'], data['email'], data['password'])
    return jsonify({"mensagem": "Voluntário criado com sucesso"}), 201

@voluntario_routes.route('/voluntarios', methods=['GET'])
def listar_voluntarios_route():
    voluntarios = buscar_voluntarios()
    return jsonify(voluntarios)

@voluntario_routes.route('/voluntarios/<externalUuid>', methods=['GET'])
def buscar_voluntario_por_id_route(externalUuid):
    voluntario = buscar_voluntario_por_id(externalUuid)
    if voluntario:
        return jsonify(voluntario)
    else:
        return jsonify({"mensagem": "Voluntário não encontrado"}), 404

@voluntario_routes.route('/voluntarios/<externalUuid>', methods=['PUT'])
def atualizar_voluntario_route(externalUuid):
    data = request.json
    atualizar_voluntario(externalUuid, data['nome'], data['CPF'], data['email'], data['password'])
    return jsonify({"mensagem": "Voluntário atualizado com sucesso"})

@voluntario_routes.route('/voluntarios/<externalUuid>', methods=['DELETE'])
def deletar_voluntario_route(externalUuid):
    deletar_voluntario(externalUuid)
    return jsonify({"mensagem": "Voluntário deletado com sucesso"})
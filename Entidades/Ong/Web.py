from flask import Blueprint, jsonify, request
from Entidades.Ong.Action import criar_ong, buscar_ongs, buscar_ong_por_id, atualizar_ong, deletar_ong

ong_routes = Blueprint('ong_routes', __name__)

@ong_routes.route('/ongs', methods=['POST'])
def criar_ong_route():
    data = request.json
    criar_ong(data['nome'], data['email'], data['razaosocial'], data['password'], data['CNPJ'])
    return jsonify({"mensagem": "ONG criada com sucesso"}), 201

@ong_routes.route('/ongs', methods=['GET'])
def listar_ongs_route():
    ongs = buscar_ongs()
    return jsonify(ongs)

@ong_routes.route('/ongs/<externalUuid>', methods=['GET'])
def buscar_ong_por_id_route(externalUuid):
    ong = buscar_ong_por_id(externalUuid)
    if ong:
        return jsonify(ong)
    else:
        return jsonify({"mensagem": "ONG não encontrada"}), 404

@ong_routes.route('/ongs/<externalUuid>', methods=['PUT'])
def atualizar_ong_route(externalUuid):
    data = request.json
    atualizar_ong(externalUuid, data['nome'], data['email'], data['razaosocial'], data['password'], data['CNPJ'])
    return jsonify({"mensagem": "ONG atualizada com sucesso"})

@ong_routes.route('/ongs/<externalUuid>', methods=['DELETE'])
def deletar_ong_route(externalUuid):
    deletar_ong(externalUuid)
    return jsonify({"mensagem": "ONG deletada com sucesso"})

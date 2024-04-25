from flask import Blueprint, jsonify, request
from Entidades.Evento.Action import criar_evento, buscar_eventos, buscar_evento_por_id, atualizar_evento, deletar_evento

evento_routes = Blueprint('evento_routes', __name__)

@evento_routes.route('/eventos', methods=['POST'])
def criar_evento_route():
    data = request.json
    criar_evento(data['tipo'], data['nome'], data['local'], data['data'], data['publico'], data['marketing'], data['fornecedores'], data['doacoes'], data['nomeOng'])
    return jsonify({"mensagem": "Evento criado com sucesso"}), 201

@evento_routes.route('/eventos', methods=['GET'])
def listar_eventos_route():
    eventos = buscar_eventos()
    return jsonify(eventos)

@evento_routes.route('/eventos/<externalUuid>', methods=['GET'])
def buscar_evento_por_id_route(externalUuid):
    evento = buscar_evento_por_id(externalUuid)
    if evento:
        return jsonify(evento)
    else:
        return jsonify({"mensagem": "Evento não encontrado"}), 404

@evento_routes.route('/eventos/<externalUuid>', methods=['PUT'])
def atualizar_evento_route(externalUuid):
    data = request.json
    atualizar_evento(externalUuid, data['tipo'], data['nome'], data['local'], data['data'], data['publico'], data['marketing'], data['fornecedores'], data['doacoes'], data['nomeOng'])
    return jsonify({"mensagem": "Evento atualizado com sucesso"})

@evento_routes.route('/eventos/<externalUuid>', methods=['DELETE'])
def deletar_evento_route(externalUuid):
    deletar_evento(externalUuid)
    return jsonify({"mensagem": "Evento deletado com sucesso"})
from flask import Blueprint, request, jsonify

player_routes = Blueprint('player_routes', __name__)

# In-memory database for demonstration purpose
players = []

# Create a player
@player_routes.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()
    player_id = len(players) + 1  # Assigning a simple ID
    player = {'id': player_id, 'name': data['name'], 'age': data['age'], 'weight': data['weight']}
    players.append(player)
    return jsonify(player), 201

# List all players
@player_routes.route('/players', methods=['GET'])
def list_players():
    return jsonify(players), 200

# Get player details
@player_routes.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = next((player for player in players if player['id'] == player_id), None)
    if player:
        return jsonify(player), 200
    return jsonify({'message': 'Player not found'}), 404

# Edit a player
@player_routes.route('/players/<int:player_id>', methods=['PUT'])
def edit_player(player_id):
    data = request.get_json()
    player = next((player for player in players if player['id'] == player_id), None)
    if player:
        player.update(data)
        return jsonify(player), 200
    return jsonify({'message': 'Player not found'}), 404

# Delete a player
@player_routes.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    global players
    players = [player for player in players if player['id'] != player_id]
    return jsonify({'message': 'Player deleted'}), 204

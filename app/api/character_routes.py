from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Character

character_routes = Blueprint('characters', __name__)

# Get all characters for the curretn user
@character_routes.route('/', methods=['GET'])
@login_required
def get_characters():
    characters = Character.query.filter_by(user_id=current_user.id).all()
    return jsonify([char.to_dict() for char in characters])

# Create a new character
@character_routes.route('/', methods=['POST'])
@login_required
def create_character():
    data = request.get.json()
    new_char = Character(
        name=data['name'],
        race=data.get('race'),
        char_class=data.get('char_class'),
        level=data.get('level', 1),
        user_id=current_user.id
    )
    db.session.add(new_char)
    db.session.commit()
    return jsonify(new_char.to_dict()), 201

# Edit a character
@character_routes.route('/<int:char_id>', methods=['PUT'])
@login_required
def update_character(char_id):
    char = Character.query.get(char_id)
    if not char or char.user_id != current_user.id:
        return jsonify({'error': 'Character not found or unathorized'}), 404
    data = request.get_json()
    char.name = data.get('name', char.name)
    char.race = data.get('race', char.race)
    char.char_class = data.get('char_class', char.char_class)
    char.level = data.get('level', char.level)
    db.session.commit()
    return jsonify(char.to_dict())

# Delete a character
@character_routes.route('/<int:char_id>', methods=['DELETE'])
@login_required

def delete_character(char_id):
    char = Character.query.get(char_id)
    if not char or char.user_id != current_user.id:
        return jsonify({'error': 'Character not found or unathorized'}), 404
    db.session.delete(char)
    db.session.commit()
    return jsonify({'message': 'Character successfully deleted!'})

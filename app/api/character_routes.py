from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Character

character_routes = Blueprint('characters', __name__)

# Get all characters for the current user
@character_routes.route('/')
@login_required
def get_all_characters():
    characters = Character.query.filter_by(user_id=current_user.id).all()
    return jsonify([character.to_dict() for character in characters]), 200

# Get a specific character by ID
@character_routes.route('/<int:id>')
@login_required
def get_character(id):
    character = Character.query.get(id)
    if character and character.user_id == current_user.id:
        return jsonify(character.to_dict()), 200
    return jsonify({"error": "Character not found or access denied"}), 404

# Create a new character
@character_routes.route('/', methods=['POST'])
@login_required
def create_character():
    data = request.get_json()
    new_character = Character(
        user_id=current_user.id,
        race_id=data['race_id'],
        background_id=data['background_id'],
        ability_scores_id=data['ability_scores_id'],
        inventory_id=data.get('inventory_id'),
        level=data.get('level', 1),
        name=data['name'],
        alignment=data.get('alignment'),
        exp=data.get('exp', 0),
        hp=data.get('hp', 0),
        ac=data.get('ac', 0),
        speed=data.get('speed', 0),
        initiative=data.get('initiative', 0),
        proficiency_bonus=data.get('proficiency_bonus', 2)  # Default proficiency bonus
    )
    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.to_dict()), 201

# Update an existing character
@character_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_character(id):
    character = Character.query.get(id)
    if not character or character.user_id != current_user.id:
        return jsonify({"error": "Character not found or access denied"}), 404
    
    data = request.get_json()
    character.name= data.get('name', character.name)
    character.level = data.get('level', character.level)
    character.alignment = data.get('alignment', character.alignment)
    character.exp = data.get('exp', character.exp)
    character.hp = data.get('hp', character.hp)
    character.ac = data.get('ac', character.ac)
    character.speed = data.get('speed', character.speed)
    character.initiative = data.get('initiative', character.initiative)
    character.proficiency_bonus = data.get('proficiency_bonus', character.proficiency_bonus)

    db.session.commit()
    return jsonify(character.to_dict()), 200

# Delete a character
@character_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_character(id):
    character = Character.query.get(id)
    if not character or character.user_id != current_user.id:
        return jsonify({"error": "Character not found or access denied"}), 404
    
    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": "Character deleted successfully"}), 200
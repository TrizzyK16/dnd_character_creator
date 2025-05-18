from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Character

character_routes = Blueprint('characters', __name__)


# Helper to convert lists to comma-separated strings
def list_to_string(value):
    return ", ".join(value) if isinstance(value, list) else value or ""


# GET /api/characters - All characters for current user
@character_routes.route('/', methods=['GET'])
@login_required
def get_all_characters():
    characters = Character.query.filter_by(user_id=current_user.id).all()
    return jsonify([char.to_dict() for char in characters]), 200


# GET /api/characters/<id> - Get one character (ownership checked)
@character_routes.route('/<int:id>', methods=['GET'])
@login_required
def get_character(id):
    character = Character.query.filter_by(id=id, user_id=current_user.id).first()
    if character:
        return jsonify(character.to_dict()), 200
    return jsonify({"error": "Character not found or access denied"}), 404

# Get characters by user_id   
@character_routes.route('/users/<int:user_id>/characters')
@login_required
def get_user_characters(user_id):
    characters = Character.query.filter_by(user_id=user_id).all()
    return jsonify([char.to_dict() for char in characters])


# POST /api/characters - Create a new character
@character_routes.route('/', methods=['POST'])
@login_required
def create_character():
    data = request.get_json()

    new_character = Character(
        user_id=current_user.id,
        name=data.get("name"),
        char_class=data.get("char_class"),
        level=data.get("level", 1),
        race=data.get("race"),
        background=data.get("background"),
        alignment=data.get("alignment", ""),
        strength=data.get("strength", 10),
        dexterity=data.get("dexterity", 10),
        constitution=data.get("constitution", 10),
        intelligence=data.get("intelligence", 10),
        wisdom=data.get("wisdom", 10),
        charisma=data.get("charisma", 10),
        armor_class=data.get("armor_class"),
        initiative=data.get("initiative"),
        speed=data.get("speed"),
        hp=data.get("hp"),
        hit_dice=data.get("hit_dice"),
        death_saves=data.get("death_saves"),
        weapon_profs=list_to_string(data.get("weapon_profs")),
        armor_profs=list_to_string(data.get("armor_profs")),
        tool_profs=list_to_string(data.get("tool_profs")),
        languages=list_to_string(data.get("languages")),
        equipment=list_to_string(data.get("equipment")),
        racial_traits=data.get("racial_traits", ""),
        class_feats=data.get("class_feats", ""),
    )

    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.to_dict()), 201


# PUT /api/characters/<id> - Update character
@character_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_character(id):
    character = Character.query.filter_by(id=id, user_id=current_user.id).first()
    if not character:
        return jsonify({"error": "Character not found or access denied"}), 404

    data = request.get_json()
    character.name = data.get("name", character.name)
    character.level = data.get("level", character.level)
    character.alignment = data.get("alignment", character.alignment)
    character.strength = data.get("strength", character.strength)
    character.dexterity = data.get("dexterity", character.dexterity)
    character.constitution = data.get("constitution", character.constitution)
    character.intelligence = data.get("intelligence", character.intelligence)
    character.wisdom = data.get("wisdom", character.wisdom)
    character.charisma = data.get("charisma", character.charisma)
    character.armor_class = data.get("armor_class", character.armor_class)
    character.initiative = data.get("initiative", character.initiative)
    character.speed = data.get("speed", character.speed)
    character.hp = data.get("hp", character.hp)
    character.hit_dice = data.get("hit_dice", character.hit_dice)
    character.weapon_profs = data.get("weapon_profs", character.weapon_profs)
    character.armor_profs = data.get("armor_profs", character.armor_profs)
    character.tool_profs = data.get("tool_profs", character.tool_profs)
    character.languages = data.get("languages", character.languages)
    character.equipment = data.get("equipment", character.equipment)
    db.session.commit()
    return jsonify(character.to_dict()), 200


# DELETE /api/characters/<id> - Delete character
@character_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_character(id):
    character = Character.query.filter_by(id=id, user_id=current_user.id).first()
    if not character:
        return jsonify({"error": "Character not found or access denied"}), 404

    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": "Character deleted successfully"}), 200

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Spell, Character

spell_routes = Blueprint('spells', __name__)

# Get all spells for a character
@spell_routes.route('/character/<int:character_id>', methods=['GET'])
@login_required
def get_spells_for_character(character_id):
    character = Character.query.get(character_id)
    if not character or character.user_id != current_user.id:
        return jsonify({'error': 'Character not found or access denied'}), 404
    
    spells = Spell.query.filter_by(character_id=character.id).all()
    return jsonify([spell.to_dict() for spell in spells]), 200

# Get a specific spell
@spell_routes.route('/<int:id>', methods=['GET'])
@login_required
def get_spell(id):
    spell = Spell.query.get(id)
    if not spell or spell.character.user_id != current_user.id:
        return jsonify({'error': 'Spell not found or access denied'}), 404
    
    return jsonify(spell.to_dict()), 200

# Create a spell
@spell_routes.route('/', methods=['POST'])
@login_required
def create_spell():
    data = request.get_json()
    character_id = data.get('character_id')
    character = Character.query.get(character_id)

    if not character or character.user_id != current_user.id:
        return jsonify({'error': 'Character not found or access denied'}), 404

    new_spell = Spell(
        character_id=character_id,
        name=data['name'],
        level=data.get('level', 0),
        school=data.get('school', ''),
        casting_time=data.get('casting_time', ''),
        spell_range=data.get('spell_range', ''),
        components=data.get('components', ''),
        duration=data.get('duration', ''),
        description=data.get('description', ''),
        higher_levels=data.get('higher_levels', '')
    )
    db.session.add(new_spell)
    db.session.commit()
    return jsonify(new_spell.to_dict()), 201

# Update a spell
@spell_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_spell(id):
    spell = Spell.query.get(id)
    if not spell or spell.character.user_id != current_user.id:
        return jsonify({'error': 'Spell not found or access denied'}), 404

    data = request.get_json()
    spell.name = data.get('name', spell.name)
    spell.level = data.get('level', spell.level)
    spell.school = data.get('school', spell.school)
    spell.casting_time = data.get('casting_time', spell.casting_time)
    spell.spell_range = data.get('range', spell.spell_range)
    spell.components = data.get('components', spell.components)
    spell.duration = data.get('duration', spell.duration)
    spell.description = data.get('description', spell.description)
    spell.higher_levels = data.get('higher_levels', spell.higher_levels)

    db.session.commit()
    return jsonify(spell.to_dict()), 200

# Delete a spell
@spell_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_spell(id):
    spell = Spell.query.get(id)
    if not spell or spell.character.user_id != current_user.id:
        return jsonify({'error': 'Spell not found or access denied'}), 404

    db.session.delete(spell)
    db.session.commit()
    return jsonify({'message': 'Spell deleted successfully'}), 200

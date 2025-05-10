from flask import Blueprint, jsonify
from app.models import Spell 

spell_routes = Blueprint('spells', __name__)

# Get all spells
@spell_routes.route('/')
def get_all_spells():
    spells = Spell.query.all()
    return jsonify([spell.to_dict() for spell in spells]), 200

# Get spell by Index
@spell_routes.route('/<string:index>', methods=['GET'])
def get_spell_by_index(index):
    spell = Spell.query.filter_by(index=index).first()
    if spell:
        return jsonify(spell.to_dict())
    return jsonify({"error": "Spell  not found"}), 404

# Get spells by char_spell_id
@spell_routes.route('/char_spells/<int:char_spell_id>', methods=['GET'])
def get_spells_by_char_spell_id(char_spell_id):
    spells = Spell.query.filter_by(char_spell_id=char_spell_id).all()
    if spells:
        return jsonify([spell.to_dict() for spell in spells])
    return jsonify({"error": "No spells found for this character"}), 404
from flask import Blueprint, jsonify
from app.models import Race
from app import db

race_routes = Blueprint('routes', __name__)

@race_routes.route('/')
def get_races():
    races = Race.query.all()
    return jsonify([
        {
            "index": race.index,
            "name": race.name,
            "speed": race.speed,
            "ability_bonuses": race.ability_bonuses,
            "age": race.age,
            "alignment": race.alignment,
            "size": race.size,
            "starting_proficiencies": race.starting_proficiencies,
            "languages": race.languages,
            "traits": race.traits,
            "subraces": race.subraces,
        } for race in races
    ])
@race_routes.route('/<string:index>')
def get_race_by_index(index):
    race = Race.query.filter_by(index=index).first()

    if race is None:
        return jsonify({'error': 'Race not found'}), 404

    return jsonify({
        "index": race.index,
        "name": race.name,
        "speed": race.speed,
        "ability_bonuses": race.ability_bonuses,
        "age": race.age,
        "alignment": race.alignment,
        "size": race.size,
        "starting_proficiencies": race.starting_proficiencies,
        "languages": race.languages,
        "traits": race.traits,
        "subraces": race.subraces,
    })
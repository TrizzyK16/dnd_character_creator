from flask import Blueprint, jsonify
from app.models import Race
from app import db

race_routes = Blueprint('routes', __name__)

@race_routes.route('/races')
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
            "size_description": race.size_description,
            "starting_proficiencies": race.starting_proficiencies,
            "languages": race.languages,
            "language_desc": race.language_desc,
            "traits": race.traits,
            "subraces": race.subraces,
            "url": race.url
        } for race in races
    ])
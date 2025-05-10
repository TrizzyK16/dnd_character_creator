from flask import Blueprint, jsonify
from app.models import RaceTrait

race_traits_routes = Blueprint('race_traits', __name__)

@race_traits_routes.route('/races/<int:race_id>')
def get_all_race_traits_by_race_id(race_id):
    race_traits = RaceTrait.query.filter_by(race_id=race_id).all()
    if not race_traits:
        return jsonify({"error": "No race traits found for this race"}), 404
    return jsonify([race_trait.to_dict() for race_trait in race_traits]), 200
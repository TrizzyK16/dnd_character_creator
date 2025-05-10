from flask import Blueprint, jsonify
from app.models import Subrace

subrace_routes = Blueprint('subraces', __name__)

@subrace_routes.route('/races/<int:race_id>')
def get_subraces_by_race_id(race_id):
    subraces = Subrace.query.filter(Subrace.race_id == race_id).all()
    if not subraces:
        return jsonify({"error": "No subraces found for this race"}), 404
    return jsonify([subrace.to_dict() for subrace in subraces]), 200
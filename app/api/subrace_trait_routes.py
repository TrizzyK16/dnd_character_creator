from flask import Blueprint, jsonify
from app.models import SubraceTrait

subrace_trait_routes = Blueprint('subrace_traits', __name__)

@subrace_trait_routes.route('/subraces/<int:subrace_id>')
def get_all_subrace_traits_by_subrace_id(subrace_id):
    subrace_traits = SubraceTrait.query.filter_by(subrace_id=subrace_id).all()
    if not subrace_traits:
        return jsonify({"error": "No subrace traits found for this subrace"}), 404
    return jsonify([subrace_trait.to_dict() for subrace_trait in subrace_traits]), 200
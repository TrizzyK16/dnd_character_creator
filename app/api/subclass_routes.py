from flask import Blueprint, jsonify
from app.models import Subclass

subclass_routes = Blueprint('subclasses', __name__)

@subclass_routes.route('/char_classes/<int:char_class_id>')
def get_subclasses_by_class_id(char_class_id):
    subclasses = Subclass.query.filter(Subclass.char_class_id == char_class_id).all()
    if not subclasses:
        return jsonify({"error": "No subclasses found for this class"}), 404
    return jsonify([subclass.to_dict() for subclass in subclasses]), 200
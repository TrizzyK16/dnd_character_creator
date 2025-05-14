from flask import Blueprint, request, jsonify
from app.models import CharClass

char_class_routes = Blueprint('classes', __name__)

# Get all character classes
@char_class_routes.route('/')
def get_all_char_classes():
    char_classes = CharClass.query.all()
    return jsonify([char_class.to_dict() for char_class in char_classes]), 200

# Get character class by Index
@char_class_routes.route('/<string:index>', methods=['GET'])
def get_char_class_by_index(index):
    char_class = CharClass.query.filter_by(index=index).first()
    if char_class:
        return jsonify(char_class.to_dict())
    return jsonify({"error": "Class not found"}), 404
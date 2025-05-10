from flask import Blueprint, jsonify
from app.models import Background

background_routes = Blueprint('backgrounds', __name__)

# Get all character classes
@background_routes.route('/')
def get_all_backgrounds():
    backgrounds = Background.query.all()
    return jsonify([background.to_dict() for background in backgrounds]), 200

# Get character class by Index
@background_routes.route('/<string:index>', methods=['GET'])
def get_background_index(index):
    background = Background.query.filter_by(index=index).first()
    if background:
        return jsonify(background.to_dict())
    return jsonify({"error": "Background not found"}), 404
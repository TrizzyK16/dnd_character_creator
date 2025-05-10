from flask import Blueprint, jsonify
from app.models import ClassFeat

class_feat_routes = Blueprint('class_feats', __name__)

# Get all class traits
@class_feat_routes.route('/char_classes/<int:class_id>')
def get_all_class_feats(class_id):
    class_feats = ClassFeat.query.filter_by(char_class_id=class_id).all()
    if not class_feats:
        return jsonify({"error": "No class feats found for this character class"}), 404
    return jsonify([class_feat.to_dict() for class_feat in class_feats]), 200
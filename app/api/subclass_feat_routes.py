from flask import Blueprint, jsonify
from app.models import SubclassFeat

subclass_feat_routes = Blueprint('subclass_feats', __name__)

# Get all subclass feats by subclass_id
@subclass_feat_routes.route('/subclasses/<int:subclass_id>')
def get_all_subclass_feats_by_subclass_id(subclass_id):
    subclass_feats = SubclassFeat.query.filter_by(subclass_id=subclass_id).all()
    if not subclass_feats:
        return jsonify({"error": "No subclass feats found for this subclass"}), 404
    return jsonify([subclass_feat.to_dict() for subclass_feat in subclass_feats]), 200
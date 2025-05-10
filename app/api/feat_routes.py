from flask import Blueprint, jsonify
from app.models import Feat

feat_routes = Blueprint('feats', __name__)

@feat_routes.route('/')
def get_all_feats():
    feats = Feat.query.all()
    return jsonify([feat.to_dict() for feat in feats]), 200

@feat_routes.route('/<string:index>', methods=['GET'])
def get_feat_by_index(index):
    feat = Feat.query.filter_by(index=index).first()
    if feat:
        return jsonify(feat.to_dict())
    return jsonify({"error": "Feat not found"}), 404

@feat_routes.route('/char_feats/<int:char_feat_id>', methods=['GET'])
def get_feats_by_char_feat_id(char_feat_id):
    feats = Feat.query.filter_by(char_feat_id=char_feat_id).all()
    if feats:
        return jsonify([feat.to_dict() for feat in feats])
    return jsonify({"error": "No feats found for this character"}), 404
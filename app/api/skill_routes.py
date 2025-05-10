from flask import Blueprint, jsonify
from app.models import Skill 

skill_routes = Blueprint('skills', __name__)

# Get all skills
@skill_routes.route('/')
def get_all_skills():
    skills = Skill.query.all()
    return jsonify([skill.to_dict() for skill in skills]), 200

# Get skill by Index
@skill_routes.route('/<string:index>', methods=['GET'])
def get_skill_by_index(index):
    skill = Skill.query.filter_by(index=index).first()
    if skill:
        return jsonify(skill.to_dict())
    return jsonify({"error": "Skill  not found"}), 404

# Get skills by char_skill_id
@skill_routes.route('/char_skills/<int:char_skill_id>', methods=['GET'])
def get_skills_by_char_skill_id(char_skill_id):
    skills = Skill.query.filter_by(char_skill_id=char_skill_id).all()
    if skills:
        return jsonify([skill.to_dict() for skill in skills])
    return jsonify({"error": "No skills found for this character"}), 404
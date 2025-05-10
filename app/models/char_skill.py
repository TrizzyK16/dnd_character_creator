from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class CharSkill(db.Model):
    __tablename__ = "char_skills"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("characters.id")), nullable=False)
    is_proficient = db.Column(db.Boolean, default=False)
    is_expertise = db.Column(db.Boolean, default=False)
    custom_bonus = db.Column(db.Integer, default=0)

    # Relationships
    character = db.relationship("Character", back_populates="char_skills")
    skills = db.relationship("Skill", back_populates="char_skill")

    def to_dict(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "is_proficient": self.is_proficient,
            "is_expertise": self.is_expertise,
            "custom_bonus": self.custom_bonus
        }
from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Skill(db.Model):
    __tablename__ = "skills"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    ability_score = db.Column(db.String, nullable=False)

    # Relationships

    def to_dict(self):
        return {
            "id": self.id,
            "char_skill_id": self.char_skill_id,
            "index": self.index,
            "name": self.name,
            "ability_score": self.ability_score
        }
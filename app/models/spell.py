from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Spell(db.Model):
    __tablename__ = "spells"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    char_spell_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("char_spells.id")), nullable=False)

    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    char_spell = db.relationship("CharSpell", back_populates="spells")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "level": self.level,
            "description": self.description,
            "char_spell_id": self.char_spell_id
        }
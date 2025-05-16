from .db import db, environment, SCHEMA, add_prefix_for_prod

class Spell(db.Model):
    __tablename__ = 'spells'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer)
    school = db.Column(db.String(100))
    casting_time = db.Column(db.String(100))
    spell_range = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    components = db.Column(db.String(255))
    description = db.Column(db.Text)
    higher_levels = db.Column(db.Text)
    character_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id')), nullable=False)

    # Relationships
    character = db.relationship("Character", back_populates="spells")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "school": self.school,
            "casting_time": self.casting_time,
            "spell_range": self.spell_range,
            "duration": self.duration,
            "components": self.components,
            "description": self.description,
            "higher_levels": self.higher_levels,
            "character_id": self.character_id
        }

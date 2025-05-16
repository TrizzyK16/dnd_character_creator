from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Race(db.Model):
    __tablename__ = "races"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    # subrace_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("subraces.id")), nullable=False)
    index = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    creature_type = db.Column(db.String)
    size = db.Column(db.Text)
    speed = db.Column(db.Integer)
    ability_bonuses = db.Column(db.JSON)
    age = db.Column(db.Text)
    alignment = db.Column(db.Text)
    starting_proficiencies = db.Column(db.JSON)
    languages = db.Column(db.JSON)
    traits = db.Column(db.JSON)

    # Relationships
    race_traits = db.relationship("RaceTrait", back_populates="race", cascade="all, delete-orphan")
    subraces = db.relationship("Subrace", back_populates="race", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "creature_type": self.creature_type,
            "size": self.size,
            "speed": self.speed,
            "ability_bonuses": self.ability_bonuses,
            "age": self.age,
            "alignment": self.alignment,
            # "size_description": self.size_description,
            "starting_proficiencies": self.starting_proficiencies,
            "languages": self.languages,
            "traits": self.traits,
            # "language_desc": self.language_desc,
        }
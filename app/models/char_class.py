from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class CharClass(db.Model):
    __tablename__ = "classes"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    index = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    hit_dice = db.Column(db.String, nullable=False)
    hp = db.Column(db.String, nullable=False)
    proficiencies = db.Column(db.JSON, nullable=False)
    starting_equipment = db.Column(db.JSON, nullable=False)

    # Relationships
    class_feats = db.relationship("ClassFeat", back_populates="char_class", cascade="all, delete-orphan")
    subclass = db.relationship("Subclass", back_populates="char_class", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "description": self.description,
            "hit_dice": self.hit_dice,
            "hp": self.hp,
            "proficiencies": self.proficiencies,
            "starting_equipment": self.starting_equipment,
            # "character_id": self.character_id
        }
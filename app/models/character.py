from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Character(db.Model):
    __tablename__ = 'characters' # Name of the table in the db

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("races.id")), nullable=False)
    background_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("backgrounds.id")), nullable=False)
    # ability_scores_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("ability_scores.id")), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("inventories.id")))
    level = db.Column(db.Integer, default=1)
    name = db.Column(db.String(50), nullable=False)
    alignment = db.Column(db.String)
    exp = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    ac = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    initiative = db.Column(db.Integer)
    proficiency_bonus = db.Column(db.Integer)
    ability_scores = db.Column(db.JSON)

    # Relationships
    user = db.relationship("User", back_populates="character")
    race = db.relationship("Race", back_populates="character")
    char_classes = db.relationship("CharClass", back_populates="character")
    background = db.relationship("Background", back_populates="character")
    # ability_scores = db.relationship("AbilityScore", back_populates="character")
    inventory = db.relationship("Inventory", back_populates="character", uselist=False)
    char_feat = db.relationship("CharFeat", back_populates="character")
    char_spell = db.relationship("CharSpell", back_populates="character")
    char_skills = db.relationship("CharSkill", back_populates="character")
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "alignment": self.alignment,
            "exp": self.exp,
            "hp": self.hp,
            "ac": self.ac,
            "speed": self.speed,
            "initiative": self.initiative,
            "proficiency_bonus": self.proficiency_bonus,
            "ability_scores": self.ability_scores,
            "user_id": self.user_id,
            "race_id": self.race_id,
            "background_id": self.background_id,
            "inventory_id": self.inventory_id
            # "ability_scores_id": self.ability_scores_id,
        }

from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class RaceTrait(db.Model):
    __tablename__ = "race_traits"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("races.id")), nullable=False)

    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    level_req = db.Column(db.Integer)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    race = db.relationship("Race", back_populates="race_traits")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "level_req": self.level_req,
            "description": self.description,
            "race_id": self.race_id
        }
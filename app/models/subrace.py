from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Subrace(db.Model):
    __tablename__ = "subraces"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("races.id")), nullable=False)
    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    race = db.relationship("Race", back_populates="subraces")
    subrace_traits = db.relationship("SubraceTrait", back_populates="subrace", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "race_id": self.race_id,
            "index": self.index,
            "name": self.name,
            "description": self.description
        }
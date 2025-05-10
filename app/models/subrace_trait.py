from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class SubraceTrait(db.Model):
    __tablename__ = "subrace_traits"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    subrace_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("subraces.id")), nullable=False)

    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    level_req = db.Column(db.Integer)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    subrace = db.relationship("Subrace", back_populates="subrace_traits")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "level_req": self.level_req,
            "description": self.description,
            "subrace_id": self.subrace_id
        }
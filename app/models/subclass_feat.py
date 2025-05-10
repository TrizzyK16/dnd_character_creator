from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class SubclassFeat(db.Model):
    __tablename__ = "subclass_feats"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    subclass_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("subclasses.id")))

    index = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    level_req = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    subclass = db.relationship("Subclass", back_populates="subclass_feats")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "level_req": self.level_req,
            "description": self.description,
            "subclass_id": self.subclass_id
        }
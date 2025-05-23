from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Feat(db.Model):
    __tablename__ = "feats"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    req = db.Column(db.String)
    description = db.Column(db.Text, nullable=False)

    # Relationships


    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "req": self.req,
            "description": self.description,
            "char_feat_id": self.char_feat_id
        }
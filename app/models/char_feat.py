from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class CharFeat(db.Model):
    __tablename__ = "char_feats"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    # Relationships

    def to_dict(self):
        return {
            "id": self.id
        }
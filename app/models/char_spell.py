from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class CharSpell(db.Model):
    __tablename__ = "char_spells"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String, nullable=False, unique=True)

    # Relationships


    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index
        }
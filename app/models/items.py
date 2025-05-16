from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Item(db.Model):
    __tablename__ = "items"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rarity = db.Column(db.Text, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    # Relationships

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "description": self.description,
            "subrace_id": self.subrace_id
        }
from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Inventory(db.Model):
    __tablename__ = "inventories"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relationships
    character = db.relationship("Character", back_populates="inventory", cascade="all, delete-orphan")
    items = db.relationship("Item", back_populates="inventory", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
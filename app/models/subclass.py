from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Subclass(db.Model):
    __tablename__ = "subclasses"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    char_class_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("classes.id")))

    index = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    char_class = db.relationship("CharClass", back_populates="subclass")
    subclass_feats = db.relationship("SubclassFeat", back_populates="subclass", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "description": self.description,
            "char_class_id": self.char_class_id
        }
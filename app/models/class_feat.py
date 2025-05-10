from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class ClassFeat(db.Model):
    __tablename__ = "class_feats"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("classes.id")))

    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    level_req = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Relationships
    char_class = db.relationship("CharClass", back_populates="class_feats")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "level_req": self.level_req,
            "description": self.description,
            "class_id": self.class_id
        }
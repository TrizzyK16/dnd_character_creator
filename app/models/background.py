from .db import db, environment, SCHEMA
# from sqlalchemy.orm import relationship

class Background(db.Model):
    __tablename__ = "backgrounds"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    skill_prof = db.Column(db.JSON)
    tool_prof = db.Column(db.JSON)
    languages = db.Column(db.JSON)
    equipment = db.Column(db.JSON)

    # Relationships
    character = db.relationship("Character", back_populates="background", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "index": self.index,
            "name": self.name,
            "description": self.description,
            "skill_prof": self.skill_prof,
            "tool_prof": self.tool_prof,
            "languages": self.languages,
            "equipment": self.equipment
        }
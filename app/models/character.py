from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Character(db.Model):
    __tablename__ = 'characters' # Name of the table in the db

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    race = db.Column(db.String(20))
    char_class = db.Column(db.String(50))
    level = db.Column(db.Integer, default=1)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="characters")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "race": self.race,
            "char_class": self.char_class,
            "level": self.level,
            "user_id": self.user_id
        }

from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text

def seed_characters():
    char1 = Character(
        name='Aelar Moonshadow',
        level=1,
        alignment="Good",
        exp=0,
        hp=10,
        ac=15,
        speed=30,
        initiative=2,
        proficiency_bonus=2,
        ability_scores={
            "str": 8, "dex": 14, "con": 13, "int": 15, "wis": 10, "cha": 12
        },
        user_id=1,
        race_id=2,
        background_id=1
    )
    # char2 = Character(
    #     name='Jonathan Goodfellow',
    #     race='Halfing',
    #     char_class='Cleric',
    #     level=2,
    #     user_id=2
    # )
    # char3 = Character(
    #     name='Baron Picklewhistle Von BrambleBottom',
    #     race='Aasamir',
    #     char_class='Druid',
    #     level=1,
    #     user_id=3
    # )

    db.session.add(char1)
    # db.session.add(char2)
    # db.session.add(char3)
    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))
        
    db.session.commit()
from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text

def seed_charcters():
    char1 = Character(
        name='Aelar Moonshadow',
        race='Elf',
        char_class='Rogue',
        level=3,
        user_id=1
    )
    char2 = Character(
        name='Jonathan Goodfellow',
        race='Halfing',
        char_class='Cleric',
        level=2,
        user_id=2
    )
    char3 = Character(
        name='Baron Picklewhistle Von BrambleBottom',
        race='Aasamir',
        char_class='Druid',
        level=1,
        user_id=3
    )

    db.session.add(char1)
    db.session.add(char2)
    db.session.add(char3)
    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))
        
    db.session.commit()
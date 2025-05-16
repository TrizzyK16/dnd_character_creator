from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text

def seed_characters():
    char1 = Character(
        user_id=1,
        name="Thalor Stormblade",
        char_class="Fighter",
        level=5,
        race="Half-Orc",
        background="Soldier",
        alignment="Chaotic Good",
        strength=18,
        dexterity=14,
        constitution=16,
        intelligence=10,
        wisdom=12,
        charisma=8,
        armor_class=17,
        initiative=2,
        speed=30,
        hp=45,
        hit_dice="5d10",
        death_saves="0/3",
        weapon_profs="Simple, Martial",
        armor_profs="All armor, shields",
        tool_profs="Smith's tools",
        languages="Common, Orc",
        equipment="Greatsword, chain mail, adventurer's pack",
        racial_traits="Darkvision, Relentless Endurance, Savage Attacks"
    )
    

    db.session.add(char1)
    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))
        
    db.session.commit()
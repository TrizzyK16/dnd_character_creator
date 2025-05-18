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
        racial_traits={
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.", 
            "relentlessEndurance": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. Once you use this trait, you can&apos;t do so again until you finish a long rest.", 
            "adrenalineRush": "You can take the Dash action as a bonus action. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. Whenever you use this trait, you gain a number of temporary hit points equal to your proficiency bonus.",
            "powerfulBuild": "You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift."
        },
        class_feats={}
    )
    

    db.session.add(char1)
    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))
        
    db.session.commit()
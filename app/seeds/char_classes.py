from app.models import db, CharClass, environment, SCHEMA
from sqlalchemy.sql import text

def seed_char_classes():
    class1 = CharClass(
        index = "artificer",
        name = "Artificer",
        description = """Masters of invention, artificers use ingenuity 
        and magic to unlock extraordinary capabilities in objects. They 
        see magic as a complex system waiting to be decoded and then 
        harnessed in their spells and inventions. You can find everything 
        you need to play one of these inventors in the next few sections. 
        Artificers use a variety of tools to channel their arcane power. 
        To cast a spell, an artificer might use alchemist's supplies to 
        create a potent elixir, calligrapher's supplies to inscribe a sigil 
        of power, or tinker's tools to craft a temporary charm. The magic of 
        artificers is tied to their tools and their talents, and few other 
        characters can produce the right tool for a job as well as an 
        artificer.""",
        hit_dice = "1d8 per artificer level",
        hp = "8 + your Con modifier",
        proficiencies = {
            "armor": ["Light armor", "medium armor", "shields"],
            "weapons": ["Simple weapons"],
            "tools": ["Thieves tools", "Tinkers tools", "one type of artins tools of your choice"],
            "savingThrows": ["Con", "Int"],
            "Skills": {
                "chooseTwo": ["Arcana", "History", "Investigation", "Medicine", "Nature", "Perception", "Sleight of Hand"]
            }
        },
        starting_equipment = ["any two simple weapons", "a light crossbow", "20 bolts", "studded leather armor or scale mail", "theives tools", "dugneoneers pack"]
    )
    # class2 = CharClass(
    #     charcter_id = 1,
    #     index = "",
    #     name = "",
    #     description = """""",
    #     hit_dice = "",
    #     hp = "",
    #     proficiencies = [],
    #     starting_equipment = []
    # )
    # class3 = CharClass(
    #     charcter_id = 1,
    #     index = "",
    #     name = "",
    #     description = """""",
    #     hit_dice = "",
    #     hp = "",
    #     proficiencies = [],
    #     starting_equipment = []
    # )

    # class1 = CharClass(
    #     charcter_id = 1,
    #     index = "",
    #     name = "",
    #     description = """""",
    #     hit_dice = "",
    #     hp = "",
    #     proficiencies = [],
    #     starting_equipment = []
    # )

    db.session.add(class1)
    db.session.commit()

def undo_char_classes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.classes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM classes"))
        
    db.session.commit()
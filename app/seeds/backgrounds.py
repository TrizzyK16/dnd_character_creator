from app.models import db, Background, environment, SCHEMA
from sqlalchemy.sql import text

def seed_backgrounds():
    background1 = Background(
        index = "acolyte",
        name = "Acolyte",
        description = "You have spent your life in the service of a temple to a specific god or pantheon of gods. You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices in order to conduct worshipers into the presence of the divine. You are not necessarily a cleric; performing sacred rites is not the same thing as channeling divine power. Choose a god, a pantheon of gods, or some other quasi-divine being, and work with your DM to detail the nature of your religious service. Were you a lesser functionary in a temple, raised from childhood to assist the priests in the sacred rites? Or were you a high priest who suddenly experienced a call to serve your god in a different way? Perhaps you were the leader of a small cult outside of any established temple structure, or even an occult group that served a fiendish master that you now deny.",
        skill_prof = ["Insight", "Religion"],
        tool_prof = ["None"],
        languages = ["Two of your choice"],
        equipment = ["Holy symbol", "Prayer book or prayer wheel", "5 sticks of incense", "Vestments", "A set of common clothes", "15gp"]
    )
    background2 = Background(
        index = "anthropologist",
        name = "Anthropologist",
        description = "You have always been fascinated by other cultures, from the most ancient and primeval lost lands to the most modern civilizations. By studying other cultures' customs, philosophies, laws, rituals, religious beliefs, languages, and art, you have learned how tribes, empires, and all forms of society in between craft their own destinies and doom. This knowledge came to you not only through books and scrolls, but also through firsthand observation by visiting far-flung settlements and exploring local histories and customs.",
        skill_prof = ["Insight", "Religion"],
        tool_prof = ["None"],
        languages = ["Two of your choice"],
        equipment = ["Leather-bound diary", "bottle of in", "ink pen", "set of travelers clothes", "1 trinket of special significance", "10gp"]
    )
    background3 = Background(
        index = "archaeologist",
        name = "Archaeologist",
        description = "An archaeologist learns about the long-lost and fallen cultures of the past by studying their remains; their bones, their ruins, their surviving masterworks, and their tombs. Those who practice archaeology travel to the far corners of the world to root through crumbled cities and lost dungeons, digging in search of artifacts that might tell the stories of monarchs and high priests, wars and cataclysms.",
        skill_prof = ["History", "Survival"],
        tool_prof = ["Cartographers tools", "Navigators tools"],
        languages = ["One of your choice"],
        equipment = ["Wooden case containing a map to a ruin or dungeon", "Bullseye lantern", "Miners pack", "Set of traveling clothes", "Shovel", "Two-person tent", "Trinket recovered from a dig site", "25gp"]
    )
    # background = Background(
    #     index = "",
    #     name = "",
    #     description = "",
    #     skill_prof = [],
    #     tool_prof = [],
    #     languages = [],
    #     equipment = []
    # )

    db.session.add(background1)
    db.session.add(background2)
    db.session.add(background3)
    db.session.commit()

def undo_backgrounds():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.backgrounds RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM backgrounds"))
        
    db.session.commit()
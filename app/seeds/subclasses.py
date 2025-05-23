from app.models import db, Subclass, environment, SCHEMA
from sqlalchemy.sql import text

def seed_subclasses():
    alchemist = Subclass(
        index = "alchemist",
        name = "Alchemist",
        description = """An Alchemist is an expert at combining reagents 
        to produce mystical effects. Alchemists use their creations to 
        give life and to leech it away. Alchemy is the oldest of artificer 
        traditions, and its versatility has long been valued during times 
        of war and peace."""
    )
    armorer = Subclass(
        index = "armorer",
        name = "Armorer",
        description = """An artificer who specializes as an Armorer 
        modifies armor to function almost like a second skin. The armor 
        is enhanced to hone the artificer's magic, unleash potent attacks, 
        and generate a formidable defense. The artificer bonds with this 
        armor, becoming one with it even as they experiment with it and 
        refine its magical capabilities."""
    )
    artillerist = Subclass(
        index = "artillerist",
        name = "Artillerist",
        description = """An Artillerist specializes in using magic to hurl 
        energy, projectiles, and explosions on a battlefield. This
        destructive power is valued by armies in the wars on many 
        different worlds. And when war passes, some members of this 
        specialization seek to build a more peaceful world by using 
        their powers to fight the resurgence of strife. The world-hopping 
        gnome artificer Vi has been especially vocal about making things 
        right: 'It's about time we fixed things instead of blowing them 
        all to hell.'"""
    )
    battleSmith = Subclass(
        index = "battle smith",
        name = "Battle Smith",
        description = """Armies require protection, and someone has to 
        put things back together if defenses fail. A combination of 
        protector and medic, a Battle Smith is an expert at defending 
        others and repairing both materiel and personnel. To aid in 
        their work, Battle Smiths are accompanied by a steel defender, 
        a protective companion of their own creation. Many soldiers 
        tell stories of nearly dying before being saved by a Battle 
        Smith and a steel defender.

        In the world of Eberron, Battle Smiths played a key role in 
        House Cannith's work on battle constructs and the original 
        warforged, and after the Last War, these artificers led efforts 
        to aid those who were injured in the war's horrific battles."""
    )

    db.session.add(alchemist)
    db.session.add(armorer)
    db.session.add(artillerist)
    db.session.add(battleSmith)
    db.session.commit()

def undo_subclasses():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.subclasses RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM subclasses"))
        
    db.session.commit()
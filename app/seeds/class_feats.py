from app.models import db, ClassFeat, environment, SCHEMA
from sqlalchemy.sql import text

def seed_class_feat():
    artificer_feat1 = ClassFeat(
        class_id = 1,
        index = "magical tinkering",
        name = "Magical Tinkering",
        level_req = 1,
        description = """At 1st level, you've learned how to invest a spark 
        of magic into mundane objects. To use this ability, you must have 
        thieves' tools or artisan's tools in hand. You then touch a Tiny 
        nonmagical object as an action and give it one of the following 
        magical properties of your choice: 
        The object sheds bright light in a 5-foot radius and dim light for 
        an additional 5 feet. 
        Whenever tapped by a creature, the object emits a recorded message
        that can be heard up to 10 feet away. You utter the message 
        when you bestow this property on the object, and the recording can 
        be no more than 6 seconds long. 
        The object continuously emits your choice of an odor or a nonverbal 
        sound (wind, waves, chirping, or the like). The chosen phenomenon 
        is perceivable up to 10 feet away. 
        A static visual effect appears on one of the object's surfaces. 
        This effect can be a picture, up to 25 words of text, lines and 
        shapes, or a mixture of these elements, as you like. 
        The chosen property lasts indefinitely. As an action, you can touch 
        the object and end the property early. 
        You can bestow magic on multiple objects, touching one object each 
        time you use this feature, though a single object can only bear one 
        property at a time. The maximum number of objects you can affect with 
        this feature at one time is equal to your Intelligence modifier 
        (minimum of one object). If you try to exceed your maximum, the 
        oldest property immediately ends, and then the new property applies."""
    )
    artificer_feat2 = ClassFeat(
        class_id = 1,
        index = "spellcastingArtificer",
        name = "Spellcasting",
        level_req = 1,
        description = """You've studied the workings of magic and how 
        to cast spells, channeling the magic through objects. To 
        observers, you don't appear to be casting spells in a 
        conventional way; you appear to produce wonders from mundane 
        items and outlandish inventions.

        Tools Required
        You produce your artificer spell effects through your tools. 
        You must have a spellcasting focus - specifically thieves' tools 
        or some kind of artisan's tool - in hand when you cast any spell 
        with this Spellcasting feature (meaning the spell has an "M" 
        component when you cast it). You must be proficient with the tool 
        to use it in this way. See the equipment chapter in the Player's 
        Handbook for descriptions of these tools.

        After you gain the Infuse Item feature at 2nd level, you can 
        also use any item bearing one of your infusions as a spellcasting 
        focus.

        Cantrips (0-Level Spells)
        At 1st level, you know two cantrips of your choice from the 
        artificer spell list. At higher levels, you learn additional 
        artificer cantrips of your choice, as shown in the Cantrips Known 
        column of the Artificer table.

        When you gain a level in this class, you can replace one of the 
        artificer cantrips you know with another cantrip from the 
        artificer spell list.

        Preparing and Casting Spells
        The Artificer table shows how many spell slots you have to cast 
        your artificer spells. To cast one of your artificer spells of 1st 
        level or higher, you must expend a slot of the spell's level or 
        higher. You regain all expended spell slots when you finish a long 
        rest.

        You prepare the list of artificer spells that are available for you 
        to cast, choosing from the artificer spell list. When you do so, 
        choose a number of artificer spells equal to your Intelligence 
        modifier + half your artificer level, rounded down (minimum of one 
        spell). The spells must be of a level for which you have spell slots.

        For example, if you are a 5th-level artificer, you have four 1st-level 
        and two 2nd-level spell slots. With an Intelligence of 14, your list 
        of prepared spells can include four spells of 1st or 2nd level, in 
        any combination. If you prepare the 1st-level spell Cure Wounds, you 
        can cast it using a lst-level or a 2nd-level slot. Casting the spell 
        doesn't remove it from your list of prepared spells.

        You can change your list of prepared spells when you finish a 
        long rest. Preparing a new list of artificer spells requires 
        time spent tinkering with your spellcasting focuses: at least 1 
        minute per spell level for each spell on your list.

        Spellcasting Ability
        Intelligence is your spellcasting ability for your artificer 
        spells; your understanding of the theory behind magic allows 
        you to wield these spells with superior skill. You use your 
        Intelligence whenever an artificer spell refers to your 
        spellcasting ability. In addition, you use your Intelligence 
        modifier when setting the saving throw DC for an artificer 
        spell you cast and when making an attack roll with one.

        Spell save DC = 8 + your proficiency bonus + your Intelligence modifier

        Spell attack modifier = your proficiency bonus + your Intelligence modifier

        Ritual Casting
        You can cast an artificer spell as a ritual if that spell has 
        the ritual tag and you have the spell prepared."""
    )
    artificer_feat3 = ClassFeat(
        class_id = 1,
        index = "infuse item",
        name = "Infuse Item",
        level_req = 2,
        description = """Infuse Item
        At 2nd level, you've gained the ability to imbue mundane items 
        with certain magical infusions, turning those objects into 
        magic items.

        Infusions Known
        When you gain this feature, pick four artificer infusions to 
        learn. You learn additional infusions of your choice when you 
        reach certain levels in this class, as shown in the Infusions 
        Known column of the Artificer table.

        Whenever you gain a level in this class, you can replace one of 
        the artificer infusions you learned with a new one.

        Infusing an Item
        Whenever you finish a long rest, you can touch a nonmagical 
        object and imbue it with one of your artificer infusions, 
        turning it into a magic item. An infusion works on only certain
        kinds of objects, as specified in the infusion's description. 
        If the item requires attunement, you can attune yourself to it 
        the instant you infuse the item. If you decide to attune to 
        the item later, you must do so using the normal process for 
        attunement (see the attunement rules in the Dungeon Master's 
        Guide).

        Your infusion remains in an item indefinitely, but when you die, 
        the infusion vanishes after a number of days equal to your 
        Intelligence modifier (minimum of 1 day). The infusion also 
        vanishes if you replace your knowledge of the infusion.

        You can infuse more than one nonmagical object at the end of a 
        long rest; the maximum number of objects appears in the 
        Infused Items column of the Artificer table. You must touch 
        each of the objects, and each of your infusions can be in only 
        one object at a time. Moreover, no object can bear more than 
        one of your infusions at a time. If you try to exceed your 
        maximum number of infusions, the oldest infusion ends, and then 
        the new infusion applies.

        If an infusion ends on an item that contains other things, 
        like a bag of holding, its contents harmlessly appear in and 
        around its space."""
    )
    artificer_feat4 = ClassFeat(
        class_id = 1,
        index = "artificer specialist",
        name = "Artficer Specialist",
        level_req = 3,
        description = """At 3rd level, you choose the type of specialist 
        you are. Your choice grants you features at 5th, 9th and 15th level."""
    )
    artificer_feat5 = ClassFeat(
        class_id = 1,
        index = "the right tool for the job",
        name = "The Right Tool for the Job",
        level_req = 3,
        description = """At 3rd level, you've learned how to produce 
        exactly the tool you need: with thieves' tools or artisan's 
        tools in hand, you can magically create one set of artisan's 
        tools in an unoccupied space within 5 feet of you. This creation 
        requires 1 hour of uninterrupted work, which can coincide with a 
        short or long rest. Though the product of magic, the tools are 
        nonmagical, and they vanish when you use this feature again."""
    )
    artificer_feat6 = ClassFeat(
        class_id = 1,
        index = "ability score imprvement",
        name = "Ability Score Improvement",
        level_req = 4,
        description = """When you reach 4th level, 8th, 12th, 16th, 
        and 19th level, you can increase one ability score of your choice 
        by 2, or you can increase two ability scores of your choice by 1. 
        As normal, you can't increase an ability score above 20 using 
        this feature. Instead of an asi, you can also choose one feat
        from the feats list."""
    )
    artificer_feat7 = ClassFeat(
        class_id = 1,
        index = "tool expertise",
        name = "Tool Expertise",
        level_req = 6,
        description = """At 6th level, your proficiency bonus is now 
        doubled for any ability check you make that uses your proficiency 
        with a tool."""
    )
    artificer_feat8 = ClassFeat(
        class_id = 1,
        index = "flash of genius",
        name = "Flash of Genius",
        level_req = 7,
        description = """At 7th level, you've gained the ability to come 
        up with solutions under pressure. When you or another creature 
        you can see within 30 feet of you makes an ability check or a 
        saving throw, you can use your reaction to add your Intelligence 
        modifier to the roll.

        You can use this feature a number of times equal to your 
        Intelligence modifier (minimum of once). You regain all 
        expended uses when you finish a long rest."""
    )
    artificer_feat9 = ClassFeat(
        class_id = 1,
        index = "magic item adept",
        name = "Magic Item Adept",
        level_req = 10,
        description = """When you reach 10th level, you achieve a 
        profound understanding of how to use and make magic items:

        You can attune to up to four magic items at once.
        If you craft a magic item with a rarity of common or uncommon, 
        it takes you a quarter of the normal time, and it costs you 
        half as much of the usual gold."""
    )
    artificer_feat10 = ClassFeat(
        class_id = 1,
        index = "spell-storing item",
        name = "Spell-Storing Item",
        level_req = 11,
        description = """At 11th level, you can now store a spell in an 
        object. Whenever you finish a long rest, you can touch one 
        simple or martial weapon or one item that you can use as a 
        spellcasting focus, and you store a spell in it, choosing a 
        1st- or 2nd-level spell from the artificer spell list that 
        requires 1 action to cast (you needn't have it prepared).

        While holding the object, a creature can take an action to 
        produce the spell's effect from it, using your spellcasting 
        ability modifier. If the spell requires concentration, the 
        creature must concentrate. The spell stays in the object until 
        it's been used a number of times equal to twice your Intelligence 
        modifier (minimum of twice) or until you use this feature again 
        to store a spell in an object."""
    )
    artificer_feat11 = ClassFeat(
        class_id = 1,
        index = "magic item savant",
        name = "Magic Item Savant",
        level_req = 14,
        description = """At 14th level, your skill with magic items 
        deepens more:

        You can attune to up to five magic items at once.
        You ignore all class, race, spell and level requirements on 
        attuning to or using a magic item."""
    )
    artificer_feat12 = ClassFeat(
        class_id = 1,
        index = "magic item master",
        name = "Magic Item Master",
        level_req = 18,
        description = """Starting at 18th level, you can attune up 
        to six magic items at once"""
    )
    artificer_feat13 = ClassFeat(
        class_id = 1,
        index = "soul of artifice",
        name = "Soul of Artifice",
        level_req = 20,
        description = """At 20th level, you develop a mystical 
        connection to your magic items, which you can draw on for 
        protection:

        You gain a +1 bonus to all saving throws per magic item you are 
        currently attuned to.
        If you're reduced to 0 hit points but not killed out-right, you 
        can use your reaction to end one of your artificer infusions, 
        causing you to drop to 1 hit point instead of 0."""
    )

    # class_feats1 = ClassFeat(
    #     class_id = ,
    #     index = "",
    #     name = "",
    #     level_req = ,
    #     description = """"""
    # )
    db.session.add(artificer_feat1)
    db.session.add(artificer_feat2)
    db.session.add(artificer_feat3)
    db.session.add(artificer_feat4)
    db.session.add(artificer_feat5)
    db.session.add(artificer_feat6)
    db.session.add(artificer_feat7)
    db.session.add(artificer_feat8)
    db.session.add(artificer_feat9)
    db.session.add(artificer_feat10)
    db.session.add(artificer_feat11)
    db.session.add(artificer_feat12)
    db.session.add(artificer_feat13)
    db.session.commit()

def undo_class_feats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.class_feats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM class_feats"))
        
    db.session.commit()
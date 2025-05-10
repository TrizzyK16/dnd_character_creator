from app.models import db, SubclassFeat, environment, SCHEMA
from sqlalchemy.sql import text

def seed_subclass_feats():
    alchemist_feat1 = SubclassFeat(
        subclass_id = 1,
        index = "tool proficiency",
        name = "Tool Proficiency",
        level_req = 3,
        description = """When you adopt this specialization at 3rd level, 
        you gain proficiency with alchemist's supplies. If you already 
        have this proficiency, you gain proficiency with one other type 
        of artisan's tools of your choice."""
    )
    alchemist_feat2 = SubclassFeat(
        subclass_id = 1,
        index = "alchemist spells",
        name = "Alchemist spells",
        level_req = 3,
        description = """Starting at 3rd level, you always have certain 
        spells prepared after you reach particular levels in this class, 
        as shown in the Alchemist Spells table. These spells count as 
        artificer spells for you, but they do not count against the number 
        of artificer spells you prepare."""
    )
    alchemist_feat3 = SubclassFeat(
        subclass_id = 1,
        index = "experimental elixir",
        name = "Experimental Elixir",
        level_req = 3,
        description = """Beginning at 3rd level, whenever you finish a 
        long rest, you can magically produce an experimental elixir in 
        an empty flask you touch. Roll on the Experimental Elixir table 
        for the elixir's effect, which is triggered when someone drinks 
        the elixir. As an action, a creature can drink the elixir or 
        administer it to an incapacitated creature.

        You can create additional experimental elixirs by expending a 
        spell slot of 1st level or higher for each one. When you do so, 
        you use your action to create the elixir in an empty flask you 
        touch, and you choose the elixir's effect from the Experimental 
        Elixir table.

        Creating an experimental elixir requires you to have alchemist 
        supplies on your person, and any elixir you create with this 
        feature lasts until it is drunk or until the end of your next 
        long rest.

        When you reach certain levels in this class, you can make more 
        elixirs at the end of a long rest: two at 6th level and three 
        at 15th level. Roll for each elixir's effect separately. Each 
        elixir requires its own flask."""
    )
    alchemist_feat4 = SubclassFeat(
        subclass_id = 1,
        index = "alchemical savant",
        name = "Alchemical Savant",
        level_req = 5,
        description = """At 5th level, you've developed masterful command 
        of magical chemicals, enhancing the healing and damage you create 
        through them. Whenever you cast a spell using your alchemist's 
        supplies as the spellcasting focus, you gain a bonus to one roll 
        of the spell. That roll must restore hit points or be a damage 
        roll that deals acid, fire, necrotic, or poison damage, and the 
        bonus equals your Intelligence modifier (minimum of +1)."""
    )
    alchemist_feat5 = SubclassFeat(
        subclass_id = 1,
        index = "restorative reagents",
        name = "Restorative Reagents",
        level_req = 9,
        description = """Starting at 9th level, you can incorporate 
        restorative reagents into some of your works:

        Whenever a creature drinks an experimental elixir you created, 
        the creature gains temporary hit points equal to 2d6 + your 
        Intelligence modifier (minimum of 1 temporary hit point).

        You can cast Lesser Restoration without expending a spell slot and 
        without preparing the spell, provided you use alchemist's supplies 
        as the spellcasting focus. You can do so a number of times equal to 
        your Intelligence modifier (minimum of once), and you regain all 
        expended uses when you finish a long rest."""
    )
    alchemist_feat6 = SubclassFeat(
        subclass_id = 1,
        index = "chemical mastery",
        name = "Chemical Mastery",
        level_req = 15,
        description = """By 15th level, you have been exposed to so 
        many chemicals that they pose little risk to you, and you can 
        use them to quickly end certain ailments:

        You gain resistance to acid damage and poison damage, and you 
        are now immune to the poisoned condition.

        You can cast Greater Restoration and Heal without expending a 
        spell slot, without preparing the spell, and without providing 
        the material component, provided you use alchemists supplies as 
        the spellcasting focus. Once you cast either spell with this 
        feature, you can't cast that spell with it again until you 
        finish a long rest."""
    )

    armorer_feat1 = SubclassFeat(
        subclass_id = 2,
        index = "tools of the trade",
        name = "Tools of the Trade",
        level_req = 3,
        description = """When you adopt this specialization at 3rd level, 
        you gain proficiency with heavy armor. You also gain proficiency 
        with smith's tools. If you already have this tool proficiency, 
        you gain proficiency with one other type of artisan's tools of 
        your choice."""
    )
    armorer_feat2 = SubclassFeat(
        subclass_id = 2,
        index = "armorer spells",
        name = "Armorer Spells",
        level_req = 3,
        description = """Starting at 3rd level, you always have certain 
        spells prepared after you reach particular levels in this class, 
        as shown in the Armorer Spells table. These spells count as 
        artificer spells for you, but they don't count against the 
        number of artificer spells you prepare."""
    )
    armorer_feat3 = SubclassFeat(
        subclass_id = 2,
        index = "arcane armor",
        name = "Arcane Armor",
        level_req = 3,
        description = """Beginning at 3rd level, your metallurgical 
        pursuits have led to you making armor a conduit for your magic. 
        As an action, you can turn a suit of armor you are wearing 
        into Arcane Armor, provided you have smith's tools in hand.

        You gain the following benefits while wearing this armor:

        If the armor normally has a Strength requirement, the arcane 
        armor lacks this requirement for you.

        You can use the arcane armor as a spellcasting focus for your 
        artificer spells.

        The armor attaches to you and can not be removed against your 
        will. It also expands to cover your entire body, although you 
        can retract or deploy the helmet as a bonus action. The armor 
        replaces any missing limbs, functioning identically to a body 
        part it is replacing.

        You can doff or don the armor as an action.

        The armor continues to be Arcane Armor until you don another suit of armor or you die."""
    )
    armorer_feat4 = SubclassFeat(
        subclass_id = 2,
        index = "armor model",
        name = "Armor Model",
        level_req = 3,
        description = """Beginning at 3rd level, you can customize your 
        Arcane Armor. When you do so, choose one of the following armor 
        models: Guardian or Infiltrator. The model you choose gives you 
        special benefits while you wear it.

        Each model includes a special weapon. When you attack with that
        weapon, you can add your Intelligence modifier, instead of 
        Strength or Dexterity, to the attack and damage rolls.

        You can change the armor's model whenever you finish a short or 
        long rest, provided you have smith's tools in hand.

        Guardian: You design your armor to be in the front line of 
        conflict. It has the following features:

        Thunder Gauntlets: Each of the armor's gauntlets counts as a 
        simple melee weapon while you aren't holding anything in it, 
        and it deals 1d8 thunder damage on a hit. A creature hit by 
        the gauntlet has disadvantage on attack rolls against targets 
        other than you until the start of your next turn, as the armor 
        magically emits a distracting pulse when the creature attacks 
        someone else.
        Defensive Field: As a bonus action, you can gain temporary hit 
        points equal to your level in this class, replacing any 
        temporary hit points you already have. You lose these temporary 
        hit points if you doff the armor. You can use this bonus action 
        a number of times equal to your proficiency bonus, and you 
        regain all expended uses when you finish a long rest.

        Infiltrator: You customize your armor for subtle undertakings. 
        It has the following features:

        Lightning Launcher: A gemlike node appears on one of your 
        armored fists or on the chest (your choice). It counts as a 
        simple ranged weapon, with a normal range of 90 feet and a 
        long range of 300 feet, and it deals 1d6 lightning damage on 
        a hit. Once on each of your turns when you hit a creature with 
        it, you can deal an extra 1d6 lightning damage to that target.
        Powered Steps: Your walking speed increases by 5 feet.
        Dampening Field: You have advantage on Dexterity (Stealth) 
        checks. If the armor normally imposes disadvantage on such 
        checks, the advantage and disadvantage cancel each other, 
        as normal."""
    )
    armorer_feat5 = SubclassFeat(
        subclass_id = 2,
        index = "extra attack",
        name = "Extra Attack",
        level_req = 5,
        description = """Starting at 5th level, you can attack twice, 
        rather than once, whenever you take the Attack action on your turn."""
    )
    armorer_feat6 = SubclassFeat(
        subclass_id = 2,
        index = "armor modifications",
        name = "Armor Modifications",
        level_req = 9,
        description = """At 9th level, you learn how to use your artificer 
        infusions to specially modify your Arcane Armor. That armor now 
        counts as separate items for the purposes of your Infuse Items 
        feature: armor (the chest piece), boots, helmet, and the armor's 
        special weapon. Each of those items can bear one of your infusions, 
        and the infusions transfer over if you change your armor's model 
        with the Armor Model feature. In addition, the maximum number of 
        items you can infuse at once increases by 2, but those extra items 
        must be part of your Arcane Armor."""
    )
    armorer_feat7 = SubclassFeat(
        subclass_id = 2,
        index = "perfected armor",
        name = "Perfected Armor",
        level_req = 3,
        description = """At 15th level, your Arcane Armor gains 
        additional benefits based on its model, as shown below.

        Guardian: When a Huge or smaller creature you can see ends its 
        turn within 30 feet of you, you can use your reaction to 
        magically force it to make a Strength saving throw against 
        your spell save DC. On a failed save, you pull the creature up 
        to 25 feet directly to an unoccupied space. If you pull the 
        target to a space within 5 feet of you, you can make a melee 
        weapon attack against it as part of this reaction.

        You can use this reaction a number of times equal to your 
        proficiency bonus, and you regain all expended uses of it when 
        you finish a long rest.

        Infiltrator: Any creature that takes lightning damage from 
        your Lightning Launcher glimmers with magical light until the 
        start of your next turn. The glimmering creature sheds dim 
        light in a 5-foot radius, and it has disadvantage on attack 
        rolls against you, as the light jolts it if it attacks you. 
        In addition, the next attack roll against it has advantage, 
        and if that attack hits, the target takes an extra 1d6 
        lightning damage."""
    )

    artillerist_feat1 = SubclassFeat(
        subclass_id = 3,
        index = "tool proficiency",
        name = "Tool Proficiency",
        level_req = 3,
        description = """When you adopt this specialization at 3rd level, 
        you gain proficiency with woodcarver's tools. If you already have 
        this proficiency, you gain proficiency with one other type of 
        artisan's tools of your choice."""
    )
    artillerist_feat2 = SubclassFeat(
        subclass_id = 3,
        index = "artillerist spells",
        name = "Artillerist Spells",
        level_req = 3,
        description = """Starting at 3rd level, you always have certain 
        spells prepared after you reach particular levels in this class, 
        as shown in the Artillerist Spells table. These spells count as 
        artificer spells for you, but they do not count against the number 
        of artificer spells you prepare."""
    )
    artillerist_feat3 = SubclassFeat(
        subclass_id = 3,
        index = "eldritch cannon",
        name = "Eldritch Cannon",
        level_req = 3,
        description = """Also at 3rd level, you've learned how to 
        create a magical cannon. Using woodcarver's tools or smith's 
        tools, you can take an action to magically create a Small or 
        Tiny eldritch cannon in an unoccupied space on a horizontal 
        surface within 5 feet of you. A Small eldritch cannon occupies 
        its space, and a Tiny one can be held in one hand. Once you 
        create a cannon, you can't do so again until you finish a long 
        rest or until you expend a spell slot to create one. You can 
        have only one cannon at a time and can't create one while your 
        cannon is present.

        The cannon is a magical object. Regardless of size, the cannon 
        has an AC of 18 and a number of hit points equal to five times 
        your artificer level. It is immune to poison damage and psychic 
        damage. If it is forced to make an ability check or a saving 
        throw, treat all its ability scores as 10 (+0). If the mending 
        spell is cast on it, it regains 2d6 hit points. It disappears 
        if it is reduced to 0 hit points or after 1 hour. You can 
        dismiss it early as an action.

        When you create the cannon, you determine its appearance and 
        whether it has legs. You also decide which type it is, choosing 
        from the options on the Eldritch Cannons table. On each of your 
        turns, you can take a bonus action to cause the cannon to 
        activate if you are within 60 feet of it. As part of the same 
        bonus action, you can direct the cannon to walk or climb up to 
        15 feet to an unoccupied space, provided it has legs."""
    )
    artillerist_feat4 = SubclassFeat(
        subclass_id = 3,
        index = "arcane firearm",
        name = "Arcane Firearm",
        level_req = 5,
        description = """At 5th level, You know how to turn a wand, 
        staff, or rod into an arcane firearm, a conduit for your 
        destructive spells. When you finish a long rest, you can use 
        woodcarver's tools to carve special sigils into a wand, staff, 
        or rod and thereby turn it into your arcane firearm. The 
        sigils disappear from the object if you later carve them on 
        a different item. The sigils otherwise last indefinitely.

        You can use your arcane firearm as a spellcasting focus for 
        your artificer spells. When you cast an artificer spell through 
        the firearm, roll a d8, and you gain a bonus to one of the 
        spell's damage rolls equal to the number rolled."""
    )
    artillerist_feat5 = SubclassFeat(
        subclass_id = 3,
        index = "explosive cannon",
        name = "Explosive Cannon",
        level_req = 9,
        description = """Starting at 9th level, every eldritch cannon 
        you create is more destructive:

        The cannon's damage rolls all increase by 1d8.

        As an action, you can command the cannon to detonate if you 
        are within 60 feet of it. Doing so destroys the cannon and 
        forces each creature within 20 feet of it to make a Dexterity 
        saving throw against your spell save DC, taking 3d8 force 
        damage on a failed save or half as much damage on a successful 
        one."""
    )
    artillerist_feat6 = SubclassFeat(
        subclass_id = 3,
        index = "fortified position",
        name = "Fortified Position",
        level_req = 15,
        description = """By 15th level, you are a master at forming 
        well-defended emplacements using Eldritch Cannon:

        You and your allies have half cover while within 10 feet of a 
        cannon you create with Eldritch Cannon, as a result of a 
        shimmering field of magical protection that the cannon emits.

        You can now have two cannons at the same time. You can create 
        two with the same action (but not the same spell slot), and you 
        can activate both of them with the same bonus action. You 
        determine whether the cannons are identical to each other or 
        different. You can't create a third cannon while you have two."""
    )

    battle_smith_feat1 = SubclassFeat(
        subclass_id = 4,
        index = "tool proficiency",
        name = "Tool Proficency",
        level_req = 3,
        description = """When you adopt this specialization at 3rd level, 
        you gain proficiency with smith's tools. If you already have this 
        proficiency, you gain proficiency with one other type of artisan's 
        tools of your choice."""
    )
    battle_smith_feat2 = SubclassFeat(
        subclass_id = 4,
        index = "battle smith spells",
        name = "Battle Smith Spells",
        level_req = 3,
        description = """Starting at 3rd level, you always have certain 
        spells prepared after you reach particular levels in this class, 
        as shown in the Battle Smith Spells table. These spells count as 
        artificer spells for you, but they do not count against the number 
        of artificer spells you prepare."""
    )
    battle_smith_feat3 = SubclassFeat(
        subclass_id = 4,
        index = "battle ready",
        name = "Batlle Ready",
        level_req = 3,
        description = """When you reach 3rd level, your combat training 
        and your experiments with magic have paid off in two ways:

        You gain proficiency with martial weapons.

        When you attack with a magic weapon, you can use your 
        Intelligence modifier, instead of Strength or Dexterity 
        modifier, for the attack and damage rolls."""
    )
    battle_smith_feat4 = SubclassFeat(
        subclass_id = 4,
        index = "steel defender",
        name = "Steel Defender",
        level_req = 3,
        description = """By 3rd level, your tinkering has borne you a 
        faithful companion, a steel defender. It's friendly to you and 
        your companions, and it obeys your commands. See its game 
        statistics in the Steel Defender stat block, which uses your 
        proficiency bonus (PB) in several places. You determine the 
        creature's appearance and whether it has two legs or four; your 
        choice has no effect on its game statistics.

        In combat, the defender shares your initiative count, but it 
        takes its turn immediately after yours. It can move and use 
        its reaction on its own, but the only action it takes on its 
        turn is the Dodge action, unless you take a bonus action on 
        your turn to command it to take another action. That action 
        can be one in its stat block or some other action. If you are 
        incapacitated, the defender can take any action of its choice, 
        not just Dodge.

        If the Mending spell is cast on it, it regains 2d6 hit points. 
        If it has died within the last hour, you can use your smith's 
        tools as an action to revive it, provided you are within 5 
        feet of it and you expend a spell slot of 1st level or higher. 
        The steel defender returns to life after 1 minute with all its 
        hit points restored.

        At the end of a long rest, you can create a new steel defender 
        if you have smith's tools with you. If you already have a 
        defender from this feature, the first one immediately perishes. 
        The defender also perishes if you die."""
    )
    battle_smith_feat5 = SubclassFeat(
        subclass_id = 4,
        index = "extra attack",
        name = "Extra Attack",
        level_req = 5,
        description = """Starting at 5th level, you can attack twice, 
        rather than once, whenever you take the Attack action on your turn."""
    )
    battle_smith_feat6 = SubclassFeat(
        subclass_id = 4,
        index = "arcane jolt",
        name = "Arcane Jolt",
        level_req = 9,
        description = """At 9th level, you've learn new ways to channel 
        arcane energy to harm or heal. When either you hit a target 
        with a magic weapon attack or your steel defender hits a 
        target, you can channel magical energy through the strike to 
        create one of the following effects:

        The target takes an extra 2d6 force damage.

        Choose one creature or object you can see within 30 feet of 
        the target. Healing energy flows into the chosen recipient, 
        restoring 2d6 hit points to it.

        You can use this energy a number of times equal to your 
        Intelligence modifier (minimum of once), but you can do so no 
        more than once on a turn. You regain all expended uses when 
        you finish a long rest."""
    )
    battle_smith_feat7 = SubclassFeat(
        subclass_id = 4,
        index = "improved defender",
        name = "Improved Defender",
        level_req = 15,
        description = """At 15th level, your Arcane Jolt and steel 
        defender become more powerful:

        The extra damage and the healing of your Arcane Jolt both 
        increase to 4d6.

        Your steel defender gains a +2 bonus to Armor Class.

        Whenever your steel defender uses its Deflect Attack, the 
        attacker takes force damage equal to 1d4 + your Intelligence 
        modifier."""
    )

    db.session.add(alchemist_feat1)
    db.session.add(alchemist_feat2)
    db.session.add(alchemist_feat3)
    db.session.add(alchemist_feat4)
    db.session.add(alchemist_feat5)
    db.session.add(alchemist_feat6)
    db.session.add(armorer_feat1)
    db.session.add(armorer_feat2)
    db.session.add(armorer_feat3)
    db.session.add(armorer_feat4)
    db.session.add(armorer_feat5)
    db.session.add(armorer_feat6)
    db.session.add(armorer_feat7)
    db.session.add(artillerist_feat1)
    db.session.add(artillerist_feat2)
    db.session.add(artillerist_feat3)
    db.session.add(artillerist_feat4)
    db.session.add(artillerist_feat5)
    db.session.add(artillerist_feat6)
    db.session.add(battle_smith_feat1)
    db.session.add(battle_smith_feat2)
    db.session.add(battle_smith_feat3)
    db.session.add(battle_smith_feat4)
    db.session.add(battle_smith_feat5)
    db.session.add(battle_smith_feat6)
    db.session.add(battle_smith_feat7)
    db.session.commit()

def undo_subclass_feats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.subclass_feats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM subclass_feats"))
        
    db.session.commit()
from app.models import db, Race, environment, SCHEMA
from sqlalchemy.sql import text

def seed_races():
    race1 = Race(
        index = "aarakocra",
        name = "Aarakocra",
        creature_type = "Humanoid",
        size = "Aarakocra are about 5 feet tall. They have thin, lightweight bodies that weigh between 80 and 100 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Aarakocra reach maturity by age 3. Compared to humans, aarakocra do not usually live longer than 30 years.",
        alignment = "Aarakocra are usually good, and most of them are neutral. They tend to be lawful, as they value order and structure in their lives.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "flight": "Because of your wings, you have a flying speed equal to your walking speed. You can not use this flying speed if you are wearing medium or heavy armor.",
            "talons": "You have talons that you can use to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier slashing damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "windCaller": "Starting at 3rd level, you can cast the Gust of Wind spell with this trait, without requiring a material component. Once you cast the spell with this trait, you can’t do so again until you finish a long rest. You can also cast the spell using any spell slots you have of 2nd level or higher. Intelligence, Wisdom, or Charisma is your spellcasting ability for it when you cast Gust of Wind with this trait (choose when you select this race).",
            }
    )
    race2 = Race(
        index = "aasimar",
        name = "Aasimar",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Aasimar mature at the same rate as humans, but they can live up to 160 years.",
        alignment = "Imbued with celestial power, most aasimar are good. Outcast aasimar are most often neutral or even evil.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "celstialResistance": "You have resistance to necrotic damage and radiant damage.",
            "healingHands": "As an action, you can touch a creature and roll a number of d4s equal to your proficiency bonus. The creature regains a number of hit points equal to the total rolled. Once you use this trait, you can not use it again until you finish a long rest.",
            "lightBearer": "You know the Light cantrip. Charisma is your spellcasting ability for it.",
            "celestialRevalation": "When you reach 3rd level, choose one of the revelation options below. Thereafter, you can use a bonus action to unleash the celestial energy within yourself, gaining the benefits of that revelation. Your transformation lasts for 1 minute or until you end it as a bonus action. Once you transform using your revelation below, you can’t use it again until you finish a long rest:",
            "necroticShroud": "Your eyes briefly become pools of darkness, and ghostly, flightless wings sprout from your back temporarily. Creatures other than your allies within 10 feet of you that can see you must succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn. Until the transformation ends, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra damage equals your proficiency bonus.",
            "radiantConsumption": "Searing light temporarily radiates from your eyes and mouth. For the duration, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, each creature within 10 feet of you takes radiant damage equal to your proficiency bonus. Until the transformation ends, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra damage equals your proficiency bonus.",
            "radiantSoul": "Two luminous, spectral wings sprout from your back temporarily. Until the transformation ends, you have a flying speed equal to your walking speed, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra damage equals your proficiency bonus."
        }
    )
    race3 = Race(
        index = "bugbear",
        name = "Bugbear",
        creature_type = "Humanoid/Goblinoid",
        size = "Bugbears are between 6 and 8 feet tall and weigh between 250 and 350 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Bugbears reach adulthood at age 16 and live up to 80 years.",
        alignment = "Bugbears endure a harsh existence that demands each of them to remain self-sufficient, even at the expense of their fellows. They tend to be chaotic evil.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
        "darkvison": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
        "feyAncestry": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
        "longLimbed": "When you make a melee attack on your turn, your reach for it is 5 feet greater than normal.",
        "powerfulBuild": "You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
        "sneaky": "You are proficient in the Stealth skill. In addition, without squeezing, you can move through and stop in a space large enough for a Small creature.",
        "supriseAttack": "If you hit a creature with an attack roll, the creature takes an extra 2d6 damage if it has not taken a turn yet in the current combat.",
        }
    )
    race4 = Race(
        index = "centaur",
        name = "Centaur",
        creature_type = "Fey",
        size = "Centaurs stand between 6 and 7 feet tall, with their equine bodies reaching about 4 feet at the withers. Your size is Medium.",
        speed = 40,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Centaurs mature and age at about the same rate as humans.",
        alignment = "Centaurs are inclined toward neutrality. Those who join the Selesnya are more often neutral good, while those who join the Gruul are typically chaotic neutral.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "charge": "If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can immediately follow that attack with a bonus action, making one attack against the target with your hooves.",
            "equineBuild": "You count as one size larger when determining your carrying capacity and the weight you can push or drag. In addition, any climb that requires hands and feet is especially difficult for you because of your equine legs. When you make such a climb, each foot of movement costs you 4 extra feet instead of the normal 1 extra foot.",
            "hooves": "You have hooves that you can use to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier bludgeoning damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "naturalAffinity": "Your fey connection to nature gives you an intuitive connection to the natural world and the animals within it. You therefore have proficiency in one of the following skills of your choice: Animal Handling, Medicine, Nature, or Survival.",
        }
    )
    race5 = Race(
        index = "changeling",
        name = "Changeling",
        creature_type = "Fey",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Changelings mature slightly faster than humans but share a similar lifespan — typically a century or less. While a changeling can transform to conceal their age, the effects of aging affect them similarly to humans.",
        alignment = "Changelings tend toward pragmatic neutrality, and few changelings embrace evil.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
           "changelingInstincts": "Thanks to your connection to the fey realm, you gain proficiency with two of the following skills of your choice: Deception, Insight, Intimidation, Performance, or Persuasion.",
           "shapechanger": "As an action, you can change your appearance and your voice. You determine the specifics of the changes, including your coloration, hair length, and sex. You can also adjust your height and weight and can change your size between Medium and Small. You can make yourself appear as a member of another race, though none of your game statistics change. You can not duplicate the appearance of an individual you have never seen, and you must adopt a form that has the same basic arrangement of limbs that you have. Your clothing and equipment are not changed by this trait. You stay in the new form until you use an action to revert to your true form or until you die."
        }
    )
    race6 = Race(
        index = "deep gnome",
        name = "Deep Gnome",
        creature_type = "Humanoid/Gnome",
        size = "Gnomes are between 3 and 4 feet tall and weigh around 40 pounds. Your size is Small.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Gnomes mature at the same rate as humans, and most are expected to settle into adult life around the age of 40. They can live to 350 years on average, but it's not too uncommon for them to reach 500 years of age.",
        alignment = "Guarded, and suspicious of outsiders, svirfneblin are cunning and taciturn, but can be just as kind-hearted, loyal, and compassionate as their surface cousins.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 120 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "giftOfTheSvirfneblin": "Starting at 3rd level, you can cast the Disguise Self spell with this trait. Starting at 5th level, you can also cast the Nondetection spell with it, without requiring a material component. Once you cast either of these spells with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast these spells using spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).",
            "gnomishMagicResistance": "You have advantage on Intelligence, Wisdom, and Charisma saving throws against spells.",
            "svirfneblinCamouflage": "When you make a Dexterity (Stealth) check, you can make the check with advantage. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
        }
        )
    race7 = Race(
        index = "dragonborn",
        name = "Dragonborn",
        creature_type = "Humanoid",
        size = "Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80",
        alignment = "Dragonborn tend towards extremes, making a conscious choice for one side or the other between Good and Evil (represented by Bahamut and Tiamat, respectively). More side with Bahamut than Tiamat (whose non-dragon followers are mostly kobolds), but villainous dragonborn can be quite terrible indeed. Some rare few choose to devote themselves to lesser dragon deities, such as Chronepsis (Neutral), and fewer still choose to worship Io, the Ninefold Dragon, who is all alignments at once.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {}
        )
    race8 = Race(
        index = "duegar",
        name = "Duegar",
        creature_type = "Humanoid/Dwarf",
        size = "Duegar stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Duegar mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.",
        alignment = "Duergar value toil above all else. Showing emotions other than grim determination or wrath is frowned on in their culture, but they can sometimes seem joyful when at work. They have the typical dwarven appreciation for order, tradition, and impeccable craftsmanship, but their goods are purely utilitarian, disdaining aesthetic or artistic value.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 120 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "duergarMagic": "Starting at 3rd level, you can cast the Enlarge/Reduce spell with this trait, without requiring a material component. Starting at 5th level, you can also cast the Invisibility spell with it, without requiring a material component. Once you cast either of these spells with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast these spells using spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).",
            "dwarvenResistance": "You have advantage on saving throws you make to avoid or end the poisoned condition on yourself. You also have resistance to poison damage.",
            "psionicResistance": "You have advantage on saving throws you make to avoid or end the charmed or stunned condition on yourself."
        }
        )
    race9 = Race(
        index = "dwarf",
        name = "Dwarf",
        creature_type = "humanoid",
        size = "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.",
        speed = 25,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.",
        alignment = "Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvsion": "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
            "dwarvenResilience": "You have advantage on saving throws against poison, and you have resistance against poison damage.",
            "dwarvenCombatTraining": "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.",
            "toolProficiency": "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.",
            "stonecunning": "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
        }
        )
    race10 = Race(
        index = "eladrin",
        name = "Eladrin",
        creature_type = "Humanoid/Elf",
        size = "Medium",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.",
        alignment = "Each eladrin resonates with emotions captured in the Feywild in the form of seasons — affinities that affect the eladrins mood and appearance.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "feyAncestry": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
            "feyStep": "As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
            "thirdLevel": "When you reach 3rd level, your Fey Step gains an additional effect based on your season; if the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Intelligence, Wisdom, or Charisma modifier (choose when you select this race):",
            "thridLevelChoice": {
                "autumn": "Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to the creatures.",
                "winter": "When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.",
                "spring": "When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.",
                "summer": "Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your proficiency bonus."
            },
            "keenSenses": "You have proficiency in the Perception skill.",
            "trance": "You do not need to sleep, and magic can not put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness. Whenever you finish this trance, you can change your season, and you can gain two proficiencies that you do not have, each one with a weapon or a tool of your choice selected from the Players Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory, and you retain them until you finish your next long rest."
        }
        )
    race11 = Race(
        index = "elf",
        name = "Elf",
        creature_type = "Humanoid",
        size = "Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.",
        alignment = "Elves love freedom, variety, and self-expression, so they lean strongly towards the gentler aspects of chaos. They value and protect others' freedom as well as their own, and are good more often than not. Drow are an exception; their exile into the Underdark has made them vicious and dangerous. Drow are more often evil than not.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "Elven"],
        traits = {
            "darkvision": "Accustomed to twilight forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
            "feyAncestry": "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
            "trance": "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance.' While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.",
            "keenSenses": "You have proficiency in the Perception skill."
        }
        )
    race12 = Race(
        index = "fairy",
        name = "Fairy",
        creature_type = "Fey",
        size = "Small",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Fairies have a life span of about a century. ",
        alignment = "Fairies are typically chaotic neutral. They are spirited, adventurous, and not bound by strict rules, often enjoying pranks and mischievous acts. While they may not always act with malicious intent, their actions are generally driven by their own whims and desires, leading them to be considered chaotic. ",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "fairyMagic": "You know the Druidcraft cantrip.",
            "thirdLevel": "Starting at 3rd level, you can cast the Faerie Fire spell with this trait. Starting at 5th level, you can also cast the Enlarge/Reduce spell with this trait. Once you cast Faerie Fire or Enlarge/Reduce with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).", 
            "flight": "Because of your wings, you have a flying speed equal to your walking speed. You can not use this flying speed if you are wearing medium or heavy armor."
        }
        )
    race13 = Race(
        index = "firbolg",
        name = "Firbolg",
        creature_type = "Humanoid",
        size = "Firbolg are between 7 and 8 feet tall and weigh between 240 and 300 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "As humanoids related to the fey, firbolg have long lifespans. A firbolg reaches adulthood around 30, and the oldest of them can live for 500 years.",
        alignment = "As people who follow the rhythm of nature and see themselves as its caretakers, firbolg are typically neutral good. Evil firbolg are rare and are usually the sworn enemies of the rest of their kind.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "firbolgMagic": "You can cast the Detect Magic and Disguise Self spells with this trait. When you use this version of Disguise Self, you can seem up to 3 feet shorter or taller. Once you cast either of these spells with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast these spells using any spell slots you have. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).",
            "hiddenStep": "As a bonus action, you can magically turn invisible until the start of your next turn or until you attack, make a damage roll, or force someone to make a saving throw. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
            "powerfulBuild": "You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
            "speechOfBeastAndLeaf": "You have the ability to communicate in a limited manner with Beasts, Plants, and vegetation. They can understand the meaning of your words, though you have no special ability to understand them in return. You have advantage on all Charisma checks you make to influence them.",
        }
        )
    race14 = Race(
        index = "genasi(air)",
        name = "Genasi(Air)",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 35,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Genasi mature at about the same rate as humans and reach adulthood in their late teens. They live somewhat longer than humans do, up to 120 years.",
        alignment = "Independent and self-reliant, genasi tend toward a neutral alignment.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "unendingBreath": "You can hold your breath indefinitely while you are not incapacitated.",
            "lightningResistance": "You have resistance to lightning damage.",
            "mingleWithTheWind": {
                "immediate": "You know the Shocking Grasp cantrip.",
                "thridLevel": "You can cast the Feather Fall spell with this trait, without requiring a material component.",
                "fifthLevel": "You can also cast the Levitate spell with this trait, without requiring a material component.",
                "details": "Once you cast Feather Fall or Levitate with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
            }
        }
        )
    race15 = Race(
        index = "genasi(earth)",
        name = "Genasi(Earth)",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Genasi mature at about the same rate as humans and reach adulthood in their late teens. They live somewhat longer than humans do, up to 120 years.",
        alignment = "Independent and self-reliant, genasi tend toward a neutral alignment.",
        # starting_proficiencies = ["None"],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "earthWalk": "You can move across difficult terrain without expending extra movement if you are using your walking speed on the ground or a floor.",
            "mergeWithStone": {
                "immediate": "You know the Blade Ward cantrip. You can cast it as normal, and you can also cast it as a bonus action a number of times equal to your proficiency bonus, regaining all expended uses when you finish a long rest.",
                "fifthLevel": "you can cast the Pass Without Trace spell with this trait, without requiring a material component. Once you cast that spell with this trait, you can not do so again until you finish a long rest. You can also cast it using any spell slots you have of 2nd level or higher.",
                "details": "Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
            }
        }
        )
    race16 = Race(
        index = "genasi(fire)",
        name = "Genasi(Fire)",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Genasi mature at about the same rate as humans and reach adulthood in their late teens. They live somewhat longer than humans do, up to 120 years.",
        alignment = "Independent and self-reliant, genasi tend toward a neutral alignment.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "fireResistance": "You have resistance to fire damage",
            "reachToTheBlaze": {
                "immediate": "You know the Produce Flame cantrip",
                "thirdLevel": "Starting at 3rd level, you can cast the Burning Hands spell with this trait.",
                "fifthLevel": "Starting at 5th level, you can also cast the Flame Blade spell with this trait, without requiring a material component.",
                "details": "Once you cast Burning Hands or Flame Blade with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
            }
        }
        )
    race17 = Race(
        index = "genasi(water)",
        name = "Genasi(Water)",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Genasi mature at about the same rate as humans and reach adulthood in their late teens. They live somewhat longer than humans do, up to 120 years.",
        alignment = "Independent and self-reliant, genasi tend toward a neutral alignment.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkVision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "acidResistance": "You have resistance to acid damage.",
            "amphibious": "You have resitance to acid damage.",
            "callToTheWave": {
                "immediate": "You know the Acid Splash cantrip.",
                "thirdLevel": "Starting at 3rd level, you can cast the Create or Destroy Water spell with this trait.",
                "fifthLevel": "Starting at 5th level, you can also cast the Water Walk spell with this trait, without requiring a material component.",
                "details": "Once you cast Create or Destroy Water or Water Walk with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
                }

            }
        )
    race18 = Race(
        index = "githyanki",
        name = "Githyanki",
        creature_type = "Humanoid",
        size = "Gith are taller and leaner than humans, with most a slender 6 feet in height. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Gith reach adulthood in their late teens and live for about a century.",
        alignment = "Githyanki tend toward lawful evil. They are aggressive and arrogant, and they remain the faithful servants of their lich-queen, Vlaakith. Renegade githyanki tend toward chaos.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "astralKnowledge": "You can mystically access a reservoir of experiences of entities connected to the Astral Plane. Whenever you finish a long rest, you gain proficiency in one skill of your choice and with one weapon or tool of your choice, selected from the Players Handbook, as you momentarily project your consciousness into the Astral Plane. These proficiencies last until the end of your next long rest.",
            "githyankiPsionics": {
                "immediate": "You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.",
                "thirdLevel": "Starting at 3rd level, you can cast the Jump spell with this trait.",
                "fifthLevel": "Starting at 5th level, you can also cast the Misty Step spell with it.",
                "details": "Once you cast Jump or Misty Step with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race). None of these spells require spell components when you cast them with this trait."
            },
            "pyschicResilience": "You have resitance to psychic damage."
        }
        )
    race19 = Race(
        index = "githzerai",
        name = "Githzerai",
        creature_type = "Humanoid",
        size = "Gith are taller and leaner than humans, with most a slender 6 feet in height. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Gith reach adulthood in their late teens and live for about a century.",
        alignment = "Githzerai tend toward lawful neutral. Their rigorous training in psychic abilities requires an implacable mental discipline.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "githzeriPsionics": {
                "immediate": "You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.",
                "thirdLevel": "Starting at 3rd level, you can cast the Shield spell with this trait.",
                "fifthLevel": "Starting at 5th level, you can also cast the Detect Thoughts spell with it.",
                "details": "Once you cast Shield or Detect Thoughts with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race). None of these spells require spell components when you cast them with this trait."
            },
            "mentalDiscipline": "Your innate psychic defenses grant you advantage on saving throws you make to avoid or end the charmed and frightened conditions on yourself.", 
            "pyschicResilience": "You have resitance to psychic damage."
        }
        )
    race20 = Race(
        index = "gnome",
        name = "Gnome",
        creature_type = "Humanoid",
        size = "Gnomes are between 3 and 4 feet tall and weigh around 40 pounds. Your size is Small.",
        speed = 25,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Gnomes mature at the same rate as humans, and most are expected to settle into adult life around the age of 40. They can live to 350 years on average, but it's not too uncommon for them to reach 500 years of age.",
        alignment = "Gnomes are generally Good. Those who tend towards Law are sages, engineers, researchers, scholars, investigators, or inventors. Those who tend towards Chaos are often minstrels, tricksters, wanderers, or fanciful jewelers. Gnomes are light-hearted, and even the tricksters amongst them favor harmless pranks over vicious schemes.",
        # starting_proficiencies = [""],
        languages = ["Common", "Gnomish"],
        traits = {
            "darkvision": "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
            "gnomeCunning": "You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."
        }
        )
    race21 = Race(
        index = "goblin",
        name = "Goblin",
        creature_type = "Humanoid",
        size = "Goblins are between 3 and 4 feet tall and weigh between 40 and 80 pounds. Your size is Small.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Goblins reach adulthood at age 8 and live up to 60 years.",
        alignment = "Goblins are typically neutral evil, as they care only for their own needs. A few goblins might tend toward good or neutrality, but only rarely.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "feyAncestry": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
            "furyOfTheSmall": "When you damage a creature with an attack or a spell and the creatures size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your proficiency bonus. You can use this trait a number of times equal to your proficiency bonus, regaining all expended uses when you finish a long rest, and you can use it no more than once per turn.",
            "nimbleEscape": "You can take the Disengage or Hide action as a bonus action on each of your turns."
        }
        )
    race22 = Race(
        index = "goliath",
        name = "Goliath",
        creature_type = "humanoid",
        size = "Goliaths are between 7 and 8 feet tall and weigh between 280 and 340 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Goliaths have lifespans comparable to humans. They enter adulthood in their late teens and usually live less than a century.",
        alignment = "Goliath society, with its clear roles and tasks, has a strong lawful bent. The goliath sense of fairness, balanced with an emphasis on self-sufficiency and personal accountability, pushes them toward neutrality.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "littleGiant": "You have proficiency in the Athletics skill, and you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
            "mountainBorn": "You have resistance to cold damage. You also naturally acclimate to high altitudes, even if you have never been to one. This includes elevations above 20,000 feet.",
            "stonesEndurance": "You can supernaturally draw on unyielding stone to shrug off harm. When you take damage, you can use your reaction to roll a d12. Add your Constitution modifier to the number rolled and reduce the damage by that total. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
        }
        )
    race23 = Race(
        index = "grung",
        name = "Grung",
        creature_type = "Humanoid",
        size = "Grungs stand between 2 ½ and 3 ½ feet tall and average about 30 pounds. Your size is Small.",
        speed = 25,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "",
        alignment = "",
        # starting_proficiencies = [""],
        languages = ["Grung"],
        traits = {
            "climbSpeed": "Your sticky finger and toe pads give you a climb speed of 25 feet",
            "amphibous": "You can breathe air and water.",
            "poisonImmunity": "You are immune to poison damge and the poisoned condition.",
            "poisonousSkin": "Any creature that grapples you or otherwise comes into direct contact with your skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature no longer in direct contact with you can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. You can also apply this poison to any piercing weapon as part of an attack with that weapon, though when you hit the poison reacts differently. The target must succeed on a DC 12 Constitution saving throw or take 2d4 poison damage.",
            "standingLeap": "Your long jump is up to 25 feet and your high jump is up to 15 feet, with or without a running start.",
            "waterDependency": "If you fail to immerse yourself in water for at least 1 hour during a day, you suffer 1 level of exhaustion at the end of that day. You can recover from this exhaustion only through magic or by immersing yourself in water for at least 1 hour."
        }
        )
    race24 = Race(
        index = "half-elf",
        name = "Half-Elf",
        creature_type = "Humanoid",
        size = "Half-elves are more or less the same size as humans, ranging from 5 to 6 feet tall. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Half-elves age at much the same rate as humans, reaching adulthood at the age of 20. They live much longer than humans, however, often exceeding 180 years.",
        alignment = "Half-elves share the chaotic bent of their elven heritage. They both value personal freedom and creative expression, demonstrating neither love of leaders nor desire for followers. They chafe at rules, resent others' demands, and sometimes prove unreliable, or at least unpredictable. They are good and evil in equal numbers, a trait they share with their human parents.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "Thanks to your elven heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
            "feyAncestry": "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
            "halfElfVersatility": {
                "versatility": "Choose one of the following traits:",
                "skillVersatility": "You gain proficiency in two skills of your choice.",
                "elfWeaponTraining": "You have proficiency with the longsword, shortsword, shortbow and the longbow.",
                "cantrip": "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.",
                "fleetOfFoot": "Your base walking speed is 35 feet",
                "maskOfTheWild": "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.",
                "drowMagic": "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.",
                "swimSpeed": "You have a swimming speed of 30 feet."
            }
        }
        )
    race25 = Race(
        index = "half-orc",
        name = "Half-Orc",
        creature_type = "Humanoid",
        size = "Half-orcs are somewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Half-orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years.",
        alignment = "Half-orcs inherit a tendency toward chaos from their orc parents and are not strongly inclined toward good. Half-orcs raised among orcs and willing to live out their lives among them are usually evil.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
            "menacing": "You gain proficiency in the Intimidation skill.",
            "relentlessEndurance": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.",
            "savageAttacks": "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."
        }
        )
    race26 = Race(
        index = "halfing",
        name = "Halfling",
        creature_type = "Humanoid",
        size = "Halflings average about 3 feet tall and weigh about 40 pounds. Your size is small.",
        speed = 25,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century.",
        alignment = "Most halflings are lawful good. As a rule, they are good-hearted and kind, hate to see others in pain, and have no tolerance for oppression. They are also very orderly and traditional, leaning heavily on the support of their community and the comfort of the old ways.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "lucky": "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.",
            "brave": "You have advantage on saving throws against being frightened.",
            "nimble": "You can move through the space of any creature that is of a size larger than yours."
        }
        )
    race27 = Race(
        index = "harengon",
        name = "Harengon",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Harengons have a life span of about a century",
        alignment = "Most Harrengons are lawful or neutral, but they can be any alignment.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "hareTrigger": "You can add your proficiency bonus to your initiative rolls.",
            "leporineSenses": "You have proficiency in the Perception skill.",
            "luckyFootwork": "When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success. You can't use this reaction if you're prone or your speed is 0.",
            "rabbitHop": "As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, without provoking opportunity attacks. You can use this trait only if your speed is greater than 0. You can use it a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
        }
        )
    race28 = Race(
        index = "hobgoblin",
        name = "Hobgoblin",
        creature_type = "Humanoid/Goblinoid",
        size = "Hobgoblins are between 5 and 6 feet tall and weigh between 150 and 200 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Hobgoblins mature at the same rate as humans and have lifespans similar in length to theirs.",
        alignment = "Hobgoblin society is built on fidelity to a rigid, unforgiving code of conduct. As such, they tend toward lawful evil.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "feyAncestry": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
            "feyGift": {
                "immediate": "You can use this trait to take the Help action as a bonus action, and you can do so a number of times equal to your proficiency bonus. You regain all expended uses when you finish a long rest.",
                "thirdLevel": "Choose one of the options below each time you take the Help action with this trait:",
                "hospitality": "You and the creature you help each gain a number of temporary hit points equal to 1d6 plus your proficiency bonus.",
                "passage": "You and the creature you help each increase your walking speeds by 10 feet until the start of your next turn.",
                "spite": "Until the start of your next turn, the first time the creature you help hits a target with an attack roll, that target has disadvantage on the next attack roll it makes within the next minute."
            },
            "fortuneFromTheMany": "If you miss with an attack roll or fail an ability check or a saving throw, you can draw on your bonds of reciprocity to gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +3). You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
        }
        )
    race29 = Race(
        index = "human",
        name = "Human",
        creature_type = "Humanoid",
        size = "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Humans reach adulthood in their late teens and live less than a century.",
        alignment = "Humans tend toward no particular alignment. The best and the worst are found among them.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {}
        )
    race30 = Race(
        index = "kenku",
        name = "Kenku",
        creature_type = "Humanoid",
        size = "Your size is Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Kenku have shorter lifespans than humans. They reach maturity at about 12 years old and can live to 60.",
        alignment = "Kenku are chaotic creatures, rarely making enduring commitments, and they care mostly for preserving their own hides. They are generally chaotic neutral in outlook.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "expertDuplication": "When you copy writing or craftwork produced by yourself or someone else, you have advantage on any ability checks you make to produce an exact duplicate.",
            "kenkuRecall": "Thanks to your supernaturally good memory, you have proficiency in two skills of your choice. Moreover, when you make an ability check using any skill in which you have proficiency, you can give yourself advantage on the check before rolling the d20. You can give yourself advantage in this way a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
            "mimicry": "You can accurately mimic sounds you have heard, including voices. A creature that hears the sounds you make can tell they are imitations only with a successful Wisdom (Insight) check against a DC of 8 + your proficiency bonus + your Charisma modifier."
        }
        )
    race31 = Race(
        index = "kobold",
        name = "Kobold",
        creature_type = "Humanoid",
        size = "Kobolds are between 2 and 3 feet tall and weigh between 25 and 35 pounds. Your size is Small.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Kobolds reach adulthood at age 6 and can live up to 120 years but rarely do so.",
        alignment = "Kobolds are fundamentally selfish, making them evil, but their reliance on the strength of their group makes them trend toward law.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "draconicCry": "As a bonus action, you let out a cry at your enemies within 10 feet of you. Until the start of your next turn, you and your allies have advantage on attack rolls against any of those enemies who could hear you. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
            "koboldLegacy": {
                "choice": "Kobolds connection to dragons can manifest in unpredictable ways in an individual kobold. Choose one of the following legacy options for your kobold:",
                "craftiness": "You have proficiency in one of the following skills of your choice: Arcana, Investigation, Medicine, Sleight of Hand, or Survival.",
                "defiance": "You have advantage on saving throws to avoid or end the frightened condition on yourself.",
                "draconicSorcery": "You know one cantrip of your choice from the sorcerer spell list. Intelligence, Wisdom, or Charisma is your spellcasting ability for that cantrip (choose when you select this race)."
            }
        }
        )
    race32 = Race(
        index = "lizardfolk",
        name = "Lizardfolk",
        creature_type = "Humanoid",
        size = "Lizardfolk are a little bulkier and taller than humans, and their colorful frills make them appear even larger. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Lizardfolk reach maturity around age 14 and rarely live longer than 60 years.",
        alignment = "Most lizardfolk are neutral. They see the world as a place of predators and prey, where life and death are natural processes. They wish only to survive, and prefer to leave other creatures to their own devices.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "swimmingSpeed": "You have a swimming speed equal to your walking speed.",
            "bite": "You have a fanged maw that you can use to make unarmed strikes. When you hit with it, the strike deals 1d6 + your Strength modifier slashing damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "holdBreath": "You can hold your breath for up to 15 minutes at a time.",
            "hungryJaws": "You can throw yourself into a feeding frenzy. As a bonus action, you can make a special attack with your Bite. If the attack hits, it deals its normal damage, and you gain temporary hit points equal to your proficiency bonus. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
            "naturalArmor": "You have tough, scaly skin. When you are not wearing armor, your base AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shields benefits apply as normal while you use your natural armor.",
            "naturesIntuition": "Thanks to your mystical connection to nature, you gain proficiency with two of the following skills of your choice: Animal Handling, Medicine, Nature, Perception, Stealth, or Survival.",
        }
        )
    race33 = Race(
        index = "locathah",
        name = "Locathah",
        creature_type = "Humanoid",
        size = "Locathah stand between 5 and 6 feet tall and average about 150 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Locathah mature to adulthood by the age of 10 but have been known to live up to 80 years.",
        alignment = "Most locathah are true neutral or have some aspect of neutrality in their alignment. They tend toward good, coming from a culture where compassion for the downtrodden is a commonality.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "swimmingSpeed": "You have a swimming speed equal to your walking speed.",
            "naturalArmor": "You have tough, scaly skin. When you are not wearing armor, your base AC is 12 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shields benefits apply as normal while you use your natural armor.",
            "observantAndAthletic": "You have proficiency in Althetics and Perception.",
            "leviathanWill": "You have advantage on saving throws against being charmed, frightened, paralyzed, poisoned, stunned, or put to sleep.",
            "limitedAmphibousness": "You can breathe air and water, but you need to be submerged at least once every 4 hours to avoid suffocating."
        }
        )
    race34 = Race(
        index = "minotaur",
        name = "Minotaur",
        creature_type = "Humanoid",
        size = "Minotaurs average over 6 feet in height, and they have stocky builds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Minotaurs mature and age at about the same rate as humans",
        alignment = "Most minotaurs lean toward chaotic alignments, and they have a slight inclination toward evil.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "horns": "You have horns that you can use to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier piercing damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "goringRush": "Immediately after you take the Dash action on your turn and move at least 20 feet, you can make one melee attack with your Horns as a bonus action.",
            "hammeringHorns": "Immediately after you hit a creature with a melee attack as part of the Attack action on your turn, you can use a bonus action to attempt to push that target with your horns. The target must be within 5 feet of you and no more than one size larger than you. Unless it succeeds on a Strength saving throw against a DC equal to 8 + your proficiency bonus + your Strength modifier, you push it up to 10 feet away from you.",
            "labyrinthineRecall": "You always know which direction is north, and you have advantage on any Wisdom (Survival) check you make to navigate or track."
        }
        )
    race35 = Race(
        index = "orc",
        name = "Orc",
        creature_type = "Humanoid",
        size = "Orcs are usually over 6 feet tall and weigh between 230 and 280 pounds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Orcs reach adulthood at age 12 and live up to 50 years.",
        alignment = "Orcs are vicious raiders, who believe that the world should be theirs. They also respect strength above all else and believe the strong must bully the weak to ensure that weakness does not spread like a disease. They are usually chaotic evil.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "adrenalineRush": "You can take the Dash action as a bonus action. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. Whenever you use this trait, you gain a number of temporary hit points equal to your proficiency bonus.",
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "powerfulBuild": "You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
            "relentlessEndurance": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. Once you use this trait, you can not do so again until you finish a long rest."
        }
        )
    race36 = Race(
        index = "owlin",
        name = "Owlin",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Owlins typically age at a similar rate to humans, with a lifespan of around 100 years. They reach maturity around the age of 20.",
        alignment = "Owlin tend to lean towards neutral, but can be any alignment.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 120 feet of yourself as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "flight": "Thanks to your wings, you have a flying speed equal to your walking speed. You can't use this flying speed if you're wearing medium or heavy armor.",
            "silentFeathers": "You have proficiency in Stealth."
        }
        )
    race37 = Race(
        index = "satyr",
        name = "Satyr",
        creature_type = "Fey",
        size = "Satyrs range from just under 5 feet to about 6 feet in height, with generally slender builds. Your size is medium.",
        speed = 35,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Satyrs mature and age at about the same rate as humans.",
        alignment = "Satyrs delight in living a life free of the mantle of law. They gravitate toward being good, but some have devious streaks and enjoy causing dismay.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "ram": "You can use your head and horns to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier bludgeoning damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "magicResitance": "You have advantage on saving throws against spells.",
            "mirthfulLeaps": "Whenever you make a long jump or a high jump, you can roll a d8 and add the number rolled to the number of feet you cover, even when making a standing jump. This extra distance costs movement as normal.",
            "reveler": "As an embodiment of revelry, you have proficiency in the Performance and Persuasion skills, and you have proficiency with one musical instrument of your choice."
        }
        )
    race38 = Race(
        index = "sea elf",
        name = "Sea Elf",
        creature_type = "Humanoid/Elf",
        size = "Sea Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.",
        alignment = "Sea Elves are typically Chaotic Good. This alignment reflects their love of freedom, emotional expression, and a natural tendency towards generosity and grace.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "swimmingSpeed": "You have a swimming speed equal to your walking speed.",
            "childOfTheSea": "You can breathe air and water, and you have resistance to cold damage.",
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "feyAncestry": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
            "friendOfTheSea": "Aquatic animals have an extraordinary affinity with your people. You can communicate simple ideas to any Beast that has a swimming speed. It can understand your words, though you have no special ability to understand it in return.",
            "keenSenses": "You have proficiency in Perception.",
            "trance": "You do not need to sleep, and magic can not put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness. Whenever you finish this trance, you can gain two proficiencies that you do not have, each one with a weapon or a tool of your choice selected from the Players Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory, and you retain them until you finish your next long rest."
        }
        )
    race39 = Race(
        index = "shadar-kai",
        name = "Shadar-kai",
        creature_type = "Humanoid/Elf",
        size = "Shadar-kai range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old.",
        alignment = "Shadar-kai typically have a Neutral alignment. While their dark nature and exile from other elves can lead to some being more inclined towards evil or chaotic tendencies, they are not inherently aligned with any specific side.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "blessingOfTheRavenQueen": {
                "immediate": "As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
                "thirdLevel": "Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent."
            },
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "feyAncestry": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
            "keenSenses": "You have proficiency in Perception.",
            "necroticResistance": "You have resistance to necrotic damage.",
            "trance": "You do not need to sleep, and magic can not put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness. Whenever you finish this trance, you can gain two proficiencies that you don’t have, each one with a weapon or a tool of your choice selected from the Players Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory, and you retain them until you finish your next long rest."
        }
        )
    race40 = Race(
        index = "shifter",
        name = "Shifter",
        creature_type = "Humanoid",
        size = "Shifters range from 5 to almost 7 feet tall. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Shifters are quick to mature both physically and emotionally, reaching young adulthood at age 10. They rarely live to be more than 70 years old.",
        alignment = "Shifters tend toward neutrality, being more focused on survival than concepts of good and evil. A love of personal freedom can drive shifters toward chaotic alignments.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "beastialInstincts": "Channeling the beast within, you have proficiency in one of the following skills of your choice: Acrobatics, Athletics, Intimidation, or Survival.",
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "shifting": {
                "immediate": "As a bonus action, you can assume a more bestial appearance. This transformation lasts for 1 minute, until you die, or until you revert to your normal appearance as a bonus action. When you shift, you gain temporary hit points equal to 2 x your proficiency bonus. You can shift a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
                "choice": "Whenever you shift, you gain an additional benefit based on one of the following options (choose when you select this race):",
                "beasthide": "You gain 1d6 additional temporary hit points. While shifted, you have a +1 bonus to your Armor Class.",
                "longtooth": "When you shift and as a bonus action on your other turns while shifted, you can use your elongated fangs to make an unarmed strike. If you hit with your fangs, you can deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.",
                "swiftstride": "While shifted, your walking speed increases by 10 feet. Additionally, you can move up to 10 feet as a reaction when a creature ends its turn within 5 feet of you. This reactive movement does not provoke opportunity attacks.",
                "wildhunt": "While shifted, you have advantage on Wisdom checks, and no creature within 30 feet of you can make an attack roll with advantage against you unless you are incapacitated."
            }
        }
        )
    race41 = Race(
        index = "tabaxi",
        name = "Tabaxi",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Tabaxi have lifespans equivalent to humans.",
        alignment = "Tabaxi tend toward chaotic alignments, as they let impulse and fancy guide their decisions. They are rarely evil, with most of them driven by curiosity rather than greed or other dark impulses.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "climbingSpeed": "You have a climbing speed equal to your walking speed.",
            "catsClaws": "You can use your claws to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier slashing damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "catsTalent": "You have proficiency in Perception and Stealth.",
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "felineAgility": "Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can not use it again until you move 0 feet on one of your turns."
        }
        )
    race42 = Race(
        index = "tiefling",
        name = "Tiefling",
        creature_type = "Humanoid",
        size = "Tieflings are about the same size and build as humans. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Tieflings mature at the same rate as humans but live a few years longer.",
        alignment = "Tieflings might not have an innate tendency toward evil, but many of them end up there. Evil or not, an independent nature inclines many tieflings toward a chaotic alignment.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.",
            "hellishResistance": "You have resistance to fire damage."
        }
        )
    race43 = Race(
        index = "tortle",
        name = "Tortle",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Young tortles crawl for a few weeks after birth before learning to walk on two legs. They reach adulthood by the age of 15 and live an average of 50 years.",
        alignment = "Tortles tend to lead orderly, ritualistic lives. They develop customs and routines, becoming more set in their ways as they age. Most are lawful good. A few can be selfish and greedy, tending more toward evil, but it's unusual for a tortle to shuck off order in favor of chaos.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "claws": "You have claws that you can use to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier slashing damage, instead of the bludgeoning damage normal for an unarmed strike.",
            "holdBreath": "You can hold your breath for up to 1 hour.",
            "naturalArmor": "Your shell provides you a base AC of 17 (your Dexterity modifier does not affect this number). You can not wear light, medium, or heavy armor, but if you are using a shield, you can apply the shields bonus as normal.",
            "naturesItuition": "Thanks to your mystical connection to nature, you gain proficiency with one of the following skills of your choice: Animal Handling, Medicine, Nature, Perception, Stealth, or Survival.",
            "shellDefense": "You can withdraw into your shell as an action. Until you emerge, you gain a +4 bonus to your AC, and you have advantage on Strength and Constitution saving throws. While in your shell, you are prone, your speed is 0 and can not increase, you have disadvantage on Dexterity saving throws, you can not take reactions, and the only action you can take is a bonus action to emerge from your shell."
        }
        )
    race44 = Race(
        index = "triton",
        name = "Triton",
        creature_type = "Humanoid",
        size = "Tritons are slightly shorter than humans, averaging about 5 feet tall. Your size is Medium.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Tritons reach maturity around age 15 and can live up to 200 years.",
        alignment = "Tritons tend toward lawful good. As guardians of the darkest reaches of the sea, their culture pushes them toward order and benevolence.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "simmingSpeed": "You have a swimming speed equal to your walking speed.",
            "amphibous": "You can breathe air and water.",
            "controlAirAndWater": {
                "immediate": "You can cast Fog Cloud.",
                "thirdLevel": "Starting at 3rd level, you can cast the Gust of Wind spell with this trait.",
                "fifthLevel": "Starting at 5th level, you can also cast the Water Walk spell with it.",
                "details": "Once you cast any of these spells with this trait, you can not cast that spell with it again until you finish a long rest. You can also cast these spells using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).",
            },
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "emissaryOfTheSea": "You can communicate simple ideas to any Beast, Elemental, or Monstrosity that has a swimming speed. It can understand your words, though you have no special ability to understand it in return.",
            "guardianOfTheDepths": "Adapted to the frigid ocean depths, you have resistance to cold damage."
        }
        )
    race45 = Race(
        index = "verdan",
        name = "Verdan",
        creature_type = "Humanoid",
        size = "Verdan start out similar in size to the goblins they were created from, ranging from 3 to 4 feet in height. But at some point after reaching maturity, each verdan undergoes a sudden growth spurt of 2 feet or more. At 1st level, you are a small creature. When you reach 5th level, you become a medium creature.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Verdan reach adulthood at around the age 24 and it is thought that they might live to nearly 200 years old. However, because no verdan has died of old age since the race's initial creation, their upper age limits remain speculation.",
        alignment = "Verdan are generally good, although their absence of racial identity and shared history can sometimes see individual verdan become untethered from any moral or ethical framework.",
        # starting_proficiencies = [""],
        languages = ["Common", "Goblin" "One language of your choice"],
        traits = {
            "blackBloodHealing": "The black blood that is a sign of your people's connection to That-Which-Endures boosts your natural healing. When you roll either 1 or 2 on any Hit Die you spend at the end of a short rest, you can re-roll the die and must use the new roll.",
            "limitedTelepathy": "You can telepathically speak to any creature you can see within 30 feet. You don't need to share a language with the creature for it to understand your telepathy, but it must be able to understand at least one language. This process of communication is slow and limited, allowing you to transmit and receive only simple ideas and straightforward concepts.",
            "pursuasive": "Your people's lack of history makes you trustworthy and humble. You have proficiency in the Persuasion skill.",
            "telepathicInsight": "Your mind's connection to the world around you strengthens your will. You have advantage on all Wisdom and Charisma saving throws."
        }
        )
    race46 = Race(
        index = "yuan-ti",
        name = "Yuan-Ti",
        creature_type = "Humanoid",
        size = "You are Medium or Small. You choose the size when you select this race.",
        speed = 30,
        ability_bonuses = {"firstScore": 2, "secondScore": 1},
        age = "Yuan-Ti mature at the same rate as humans and have lifespans similar in length to theirs.",
        alignment = "Yuan-Ti are devoid of emotion and see others as tools to manipulate. They care little for law or chaos and are typically neutral evil.",
        # starting_proficiencies = [""],
        languages = ["Common", "One language of your choice"],
        traits = {
            "darkvision": "You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.",
            "magicResistance": "You have advantage on saving throws against spells.",
            "poisonResilience": "You have advantage on saving throws you make to avoid or end the poisoned condition on yourself. You also have resistance to poison damage.",
            "serpentineSpellcasting": {
                "immediate": "You know the Poison Spray cantrip. You can cast Animal Friendship an unlimited number of times with this trait, but you can target only snakes with it.",
                "thirdLevel": "Starting at 3rd level, you can also cast Suggestion with this trait. Once you cast it, you can not do so again until you finish a long rest. You can also cast it using any spell slots you have of 2nd level or higher.",
                "details": "Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race)."
            }
        }
        )

    db.session.add(race1)
    db.session.add(race2)
    db.session.add(race3)
    db.session.add(race4)
    db.session.add(race5)
    db.session.add(race6)
    db.session.add(race7)
    db.session.add(race8)
    db.session.add(race9)
    db.session.add(race10)
    db.session.add(race11)
    db.session.add(race12)
    db.session.add(race13)
    db.session.add(race14)
    db.session.add(race15)
    db.session.add(race16)
    db.session.add(race17)
    db.session.add(race18)
    db.session.add(race19)
    db.session.add(race20)
    db.session.add(race21)
    db.session.add(race22)
    db.session.add(race23)
    db.session.add(race24)
    db.session.add(race25)
    db.session.add(race26)
    db.session.add(race27)
    db.session.add(race28)
    db.session.add(race29)
    db.session.add(race30)
    db.session.add(race31)
    db.session.add(race32)
    db.session.add(race33)
    db.session.add(race34)
    db.session.add(race35)
    db.session.add(race36)
    db.session.add(race37)
    db.session.add(race38)
    db.session.add(race39)
    db.session.add(race40)
    db.session.add(race41)
    db.session.add(race42)
    db.session.add(race43)
    db.session.add(race44)
    db.session.add(race45)
    db.session.add(race46)
    db.session.commit()

def undo_races():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.races RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM races"))
        
    db.session.commit()
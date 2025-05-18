import { useCharacter } from "../Context/CharacterContext";
import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { useNavigate } from "react-router-dom";
import "./CharacterSheet.css";


export default function CharacterSheet({ mode = "view" }) {
    const { id } = useParams();
    const { character, setCharacter } = useCharacter();
    const [raceData, setRaceData] = useState(null);
    const [backgroundData, setBackgroundData] = useState(null);
    const [classData, setClassData] = useState(null);
    const [classFeatData, setClassFeatData] = useState(null);
    const navigate = useNavigate();

    function capitalize(str) {
        if (!str) return '';
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    function formatTrait(trait) {
        return trait
            .replace(/([A-Z])/g, ' $1')
            .replace(/^./, (str) => str.toUpperCase());
    }

    function getModifier(score) {
        return Math.floor((score - 10) / 2);
    }

    // --- Fetch race info ---
    useEffect(() => {
        if (!character?.race) return;
        fetch(`/api/races/${character.race}`)
            .then(res => res.json())
            .then(data => setRaceData(data))
            .catch(err => console.error(`Failed to fetch race data: ${err}`));
    }, [character?.race, mode]);

    // --- Fetch background info ---
    useEffect(() => {
        if (!character?.background) return;
        fetch(`/api/backgrounds/${character.background}`)
            .then(res => res.json())
            .then(data => setBackgroundData(data))
            .catch(err => console.error(`Failed to fetch background data: ${err}`));
    }, [character?.background]);

    // --- Fetch class info ---
    useEffect(() => {
        if (!character?.charClass) return;
        fetch(`/api/classes/${character.charClass}`)
            .then(res => res.json())
            .then(data => setClassData(data))
            .catch(err => console.error(`Failed to fetch class data: ${err}`));
    }, [character?.charClass, mode]);

    // --- Fetch class feat info ---
    useEffect(() => {
        if (!classData?.id) return;
        fetch(`/api/class_feats/classes/${classData.id}`)
            .then(res => res.json())
            .then(data => setClassFeatData(data))
            .catch(err => console.error(`Failed to fetch class feat data: ${err}`));
    }, [classData?.id, mode]);

    useEffect(() => {
        if (!id) return;
        fetch(`/api/characters/${id}`)
            .then(res => {
            if (!res.ok) throw new Error("Failed to fetch character");
            return res.json();
            })
            .then(data => setCharacter(data))
            .catch(err => console.error(`Failed to fetch character data: ${err}`));
        }, [id, mode, setCharacter]);
    


    if (!character || Object.keys(character).length === 0) {
        return <div>Loading character...</div>;
        }

    return (
        <div className="sheet-container">
            <header className="sheet-header">
                <h1>Character Sheet</h1>
                <div className="basic-info">
                    <div>
                        <label>Name: </label>
                        <input type="text" value={character.name || ""} readOnly />
                    </div>
                    <div>
                        <label>Class: </label>
                        <input type="text" value={capitalize(character.charClass) || capitalize(character.char_class) || "" } readOnly />
                    </div>
                    <div>
                        <label>Level: </label>
                        <input type="number" value={character.level || 1} readOnly />
                    </div>
                    <div>
                        <label>Race: </label>
                        <input type="text" value={capitalize(character.race || "")} readOnly />
                    </div>
                    <div>
                        <label>Background: </label>
                        <input type="text" value={capitalize(character.background) || ""} readOnly />
                    </div>
                    <div>
                        <label>Alignment: </label>
                        <input type="text" value={character.alignment || ""} readOnly />
                    </div>
                </div>
            </header>

            <main className="sheet-body">
                <section className="ability-scores">
                    <h2>Ability Scores</h2>
                    <div className="score-grid">
                        {["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"].map((stat) => (
                            <div className="ability" key={stat}>
                                <h3>{stat.slice(0, 3).toUpperCase()}</h3>
                                <input type="number" value={character[stat] || 10} readOnly />
                                <p>Modifier: {getModifier(character[stat] || 10)}</p>
                            </div>
                        ))}
                    </div>
                </section>

                <section className="skills-section">
                    <h2>Skills</h2>
                    <div className="skills-grid">
                        {[
                            { name: "Acrobatics", ability: "DEX" },
                            { name: "Animal Handling", ability: "WIS" },
                            { name: "Arcana", ability: "INT" },
                            { name: "Athletics", ability: "STR" },
                            { name: "Deception", ability: "CHA" },
                            { name: "History", ability: "INT" },
                            { name: "Insight", ability: "WIS" },
                            { name: "Intimidation", ability: "CHA" },
                            { name: "Investigation", ability: "INT" },
                            { name: "Medicine", ability: "WIS" },
                            { name: "Nature", ability: "INT" },
                            { name: "Perception", ability: "WIS" },
                            { name: "Performance", ability: "CHA" },
                            { name: "Persuasion", ability: "CHA" },
                            { name: "Religion", ability: "INT" },
                            { name: "Sleight of Hand", ability: "DEX" },
                            { name: "Stealth", ability: "DEX" },
                            { name: "Survival", ability: "WIS" },
                        ].map((skill) => (
                            <div className="skill" key={skill.name}>
                                <label>
                                    <input type="checkbox" disabled /> {skill.name} ({skill.ability})
                                </label>
                                <input type="number" placeholder="+0" readOnly />
                            </div>
                        ))}
                    </div>
                </section>

                <section className="combat-stats">
                    <h2>Combat</h2>
                    <div className="combat-grid">
                        <div><label>Armor Class:</label><input type="number" value={character?.armor_class || ""} readOnly /></div>
                        <div><label>Initiative:</label><input type="number" value={getModifier(character["dexterity"] || 10)} readOnly /></div>
                        <div><label>Speed:</label><input type="text" value={raceData?.speed || character?.speed || ""} readOnly /></div>
                        <div><label>HP:</label><input type="text" value={classData?.hp || character?.hp || ""} readOnly /></div>
                        <div><label>Hit Dice:</label><input type="text" value={classData?.hit_dice || character?.hit_dice || ""} readOnly /></div>
                        <div><label>Death Saves:</label><input type="text" readOnly /></div>
                    </div>
                </section>

                <section className="proficiencies">
                    <h3>Proficiencies & Languages</h3>
                    <div className="prof-section">
                        <h4>Weapons</h4>
                        <textarea rows="2" value={classData?.proficiencies?.weapons?.join(", ") || character?.weapon_profs || ""} readOnly />
                    </div>

                    <div className="prof-divider"></div>

                    <div className="prof-section">
                        <h4>Armor</h4>
                        <textarea rows="2" value={classData?.proficiencies?.armor?.join(", ") || character?.armor_profs || ""} readOnly />
                    </div>

                    <div className="prof-divider"></div>

                    <div className="prof-section">
                        <h4>Tools</h4>
                        <textarea
                            rows="2"
                            value={
                                [
                                    ...(backgroundData?.tool_prof?.[0] === "None" ? [] : backgroundData?.tool_prof || character?.tool_profs.split(",") || []),
                                    ...(classData?.proficiencies?.tools || [])
                                ].join(", ")
                            }
                            readOnly
                        />
                    </div>

                    <div className="prof-divider"></div>

                    <div className="prof-section">
                        <h4>Languages</h4>
                        <textarea
                            rows="2"
                            value={
                                [raceData?.languages, backgroundData?.languages]
                                    .flat()
                                    .filter(Boolean)
                                    .join(", ")
                                    || character.languages
                            }
                            readOnly
                        />
                    </div>
                </section>

                <section className="equipment">
                    <h2>Equipment</h2>
                    <textarea
                        rows="2"
                        value={
                            [backgroundData?.equipment, classData?.starting_equipment]
                                .flat()
                                .filter(Boolean)
                                .join(", ")
                                || character.equipment
                        }
                        readOnly
                    />
                </section>

                <section className="features-traits">
                    <h2>Features & Traits</h2>
                    <ul>
                        <h3>Racial Traits</h3>
                        {raceData?.traits &&
                            Object.entries(raceData.traits).map(([key, value]) => (
                                <li key={key}>
                                    <strong>{formatTrait(key)}:</strong> {value}
                                </li>
                            )) || 
                        character?.racial_traits &&
                            Object.entries(character.racial_traits).map(([key, value]) => (
                                <li key={key}>
                                    <strong>{formatTrait(key)}:</strong> {value}
                                </li>
                            ))
                        }
                    </ul>
                </section>

                <section className="spellcasting">
                    <h2>Spellcasting</h2>
                    <button onClick={() => navigate(`/character-sheet/${character.id}/spells/new`)}>
                        Create Spell
                    </button>
                    <button onClick={() => navigate(`/character-sheet/${character.id}/spells`)}>
                        View Spells
                    </button>
                </section>

                <button onClick={() => navigate(`/character-sheet/${character.id}/edit`)}> 
                    Edit Character
                </button>

            </main>
        </div>
    );
}

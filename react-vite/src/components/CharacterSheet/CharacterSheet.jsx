import { useCharacter } from "../Context/CharacterContext";
import { useEffect, useState } from "react";
import "./CharacterSheet.css";

export default function CharacterSheet() {
    const { character } = useCharacter();
    const [raceData, setRaceData] = useState(null);
    const [backgroundData, setBackgroundData] = useState(null);
    const [classData, setClassData] = useState(null);
    const [classFeatData, setClassFeatData] = useState(null);

    function capitalize(str) {
        if (!str) return '';
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    function formatTrait(trait) {
        // Capitalize the first letter, and add a space between the words
        const formattedKey = trait
            .replace(/([A-Z])/g, ' $1')  // Add space before uppercase letters
            .replace(/^./, (str) => str.toUpperCase());  // Capitalize the first letter
        return formattedKey;
        }


    useEffect(() => {
        if (!character.race) return <p>No character data found. Please create a character first.</p>; // If no race is selected, do nothing

        fetch(`/api/races/${character.race}`)
            .then(res => res.json())
            .then(data => setRaceData(data))
            .catch(err => console.error(`Failed to fetch race data: ${err}`))
    }, [character.race]);

    useEffect(() => {
        if (!character.background) return <p>No background data found, please try again.</p>

        fetch(`/api/backgrounds/${character.background}`)
            .then(res => res.json())
            .then(data => setBackgroundData(data))
            .catch(err => console.error(`Failed to fetch background data: ${err}`))
    }, [character.background]);

    useEffect(() => {
        if (!character.charClass) return <p>No class data found, please try again.</p>

        fetch(`/api/classes/${character.charClass}`)
            .then(res => res.json())
            .then(data => setClassData(data))
            .catch(err => console.error(`Failed to fetch class data: ${err}`))
    }, [character.charClass]);

    useEffect(() => {
        if (!classData?.id) return;

        fetch(`/api/class_feats/classes/${classData?.id}`)
            .then(res => res.json())
            .then(data => setClassFeatData(data))
            .catch(err => console.error(`Failed to fetch class feat data: ${err}`))
    }, [classData])

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
                        <input type="text" value={capitalize(character.charClass )|| ""} readOnly />
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
                        <input type="text" />
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
                        <p>Modifier</p>
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
                        <input type="checkbox" /> {skill.name} ({skill.ability})
                        </label>
                        <input type="number" placeholder="+0" />
                    </div>
                    ))}
                </div>
                </section>


                <section className="combat-stats">
                <h2>Combat</h2>
                <div className="combat-grid">
                    <div><label>Armor Class:</label><input type="number" /></div>
                    <div><label>Initiative:</label><input type="number" /></div>
                    <div><label>Speed:</label><input type="text" value={`${raceData?.speed} feet` || ""}/></div>
                    <div><label>HP:</label><input type="text" value={`${classData?.hp}`}/></div>
                    <div><label>Hit Dice:</label><input type="text" value={`${classData?.hit_dice}`}/></div>
                    <div><label>Death Saves:</label><input type="text" /></div>
                </div>
                </section>

                <section className="proficiencies">
                    <h3>Proficiencies & Languages</h3>
                    
                    <div className="prof-section">
                        <h4>Weapons</h4>
                        <textarea rows="2" value={`${classData?.proficiencies.weapons.join(", ")}`}/>
                    </div>

                    <div className="prof-divider"></div>

                    <div className="prof-section">
                        <h4>Armor</h4>
                        <textarea rows="2" value={`${classData?.proficiencies.armor.join(", ")}`}/>
                    </div>

                    <div className="prof-divider"></div>

                    <div className="prof-section">
                        <h4>Tools</h4>
                        <textarea
                            rows="2"
                            value={[
                                ...(backgroundData?.tool_prof?.[0] === "None" ? [] : backgroundData?.tool_prof || []),
                                ...(classData?.proficiencies?.tools || [])
                            ].filter(Boolean).join(", ")}
                            />
                    </div>

                    <div className="prof-divider"></div>

                    <div className="prof-section">
                        <h4>Languages</h4>
                        <textarea rows="2" value={`${raceData?.languages.join(", ")}, ${backgroundData?.languages.join(", ")}`}/>
                    </div>
                </section>

                <section className="equipment">
                <h2>Equipment</h2>
                <textarea rows="2" value={[backgroundData?.equipment.join(", "), classData?.starting_equipment.join(", ")]}/>
                </section>

                <section className="features-traits">
                    <h2>Features & Traits</h2>
                        <ul>
                            <h3>Racial Traits</h3>
                            {raceData?.traits && Object.entries(raceData.traits).map(([key, value]) => (
                                <li key={key}>
                                    <strong>{formatTrait(key)}:</strong> {value}
                                </li>
                            ))
                            }
                        </ul>
                </section>

                <section className="spellcasting">
                <h2>Spellcasting</h2>
                <textarea rows="6" />
                </section>
            </main>
        </div>
    )
}
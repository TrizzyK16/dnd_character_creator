import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useCharacter } from "../Context/CharacterContext";
import BackgroundSelector from "../Selectors/Background/BackgroundSelector"
import CharClassSelector from "../Selectors/CharClass/CharClassSelector"
import RaceSelector from "../Selectors/Race/RaceSelector"
// import SubraceSelector from "../Selectors/Subrace/SubraceSelector"
import "./CharacterBuilder.css"

export default function CharacterBuilder() {
  const { setCharacter } = useCharacter();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    level: 1,
    race: "",
    class: "",
    background: "",
    strength: 8,
    dexterity: 8,
    constitution: 8,
    intelligence: 8,
    wisdom: 8,
    charisma: 8,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({...prev, [name]: value}));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setCharacter(formData);
    navigate("/character-sheet");
  };

  return (
  <div className="builder-container">
      <h1>Create Your D&D Character!</h1>

      <form onSubmit={handleSubmit}>
        <section className="section">
            <h2>Character Info</h2>
            <div className="selector-group">
                <div className="name-container">
                  <label htmlFor="name">Name: </label>
                  <input
                    type="string"
                    id="name"
                    name="name"
                    placeholder="Character Name"
                    value={formData.name}
                    onChange={handleChange}
                  />
                </div>
                <RaceSelector onChange={handleChange}/>
                <CharClassSelector onChange={handleChange}/>
                <BackgroundSelector onChange={handleChange}/>
                <div className="level-container">
                  <label htmlFor="level">Level: </label>
                  <input
                    type="number"
                    id="level"
                    name="level"
                    min="1"
                    max="20"
                    value={formData.level}
                    onChange={handleChange}
                  />
                </div>
            </div>
          </section>

          <section className="section">
          <h2>Ability Scores</h2>
          <div className="ability-scores-row">
            <div className="ability-score">
              <label htmlFor="str">Str: </label>
              <input
                type="number"
                id="str"
                name="strength"
                min="1"
                max="20"
                value={formData.strength}
                onChange={handleChange}
              />
            </div>
            <div className="ability-score">
              <label htmlFor="dex">Dex: </label>
              <input
                type="number"
                id="dex"
                name="dexterity"
                min="1"
                max="20"
                value={formData.dexterity}
                onChange={handleChange}
              />
            </div>
            <div className="ability-score">
              <label htmlFor="con">Con: </label>
              <input
                type="number"
                id="con"
                name="constitution"
                min="1"
                max="20"
                value={formData.constitution}
                onChange={handleChange}
              />
            </div>
            <div className="ability-score">
              <label htmlFor="int">Int: </label>
              <input
                type="number"
                id="int"
                name="intelligence"
                min="1"
                max="20"
                value={formData.intelligence}
                onChange={handleChange}
              />
            </div>
            <div className="ability-score">
              <label htmlFor="wis">Wis: </label>
              <input
                type="number"
                id="wis"
                name="wisdom"
                min="1"
                max="20"
                value={formData.wisdom}
                onChange={handleChange}
              />
            </div>
            <div className="ability-score">
              <label htmlFor="cha">Cha: </label>
              <input
                type="number"
                id="cha"
                name="Charisma"
                min="1"
                max="20"
                value={formData.charisma}
                onChange={handleChange}
              />
            </div>
          </div>

        </section>

        <section className="section">
          <h2>Appearance & Backstory</h2>
          <p>[Text inputs, textarea, or pickers go here]</p>
        </section>

        <button type="submit">Finish Character</button>
      </form>
  </div>
  );
}
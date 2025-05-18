import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useCharacter } from "../Context/CharacterContext";
import BackgroundSelector from "../Selectors/Background/BackgroundSelector";
import CharClassSelector from "../Selectors/CharClass/CharClassSelector";
import RaceSelector from "../Selectors/Race/RaceSelector";
import "./CharacterBuilder.css";

export default function CharacterBuilder() {
  const { setCharacter } = useCharacter();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    level: 1,
    race: "",
    char_class: "",
    background: "",
    strength: 8,
    dexterity: 8,
    constitution: 8,
    intelligence: 8,
    wisdom: 8,
    charisma: 8,
    initiative: 0,
    speed: 30,
    hp: 0,
    hit_dice: "",
    death_saves: "0/3",
    weapon_profs: "",
    armor_profs: "",
    tool_profs: "",
    languages: "",
    equipment: "",
    racial_traits: {},
    class_feats: {},
  });

const handleChange = (e) => {
  const { name, value } = e.target;

  if (name === "charClass") {
    // Update both keys to keep them in sync
    setFormData((prev) => ({
      ...prev,
      char_class: value,
      charClass: value,
    }));
  } else if (name === "char_class") {
    setFormData((prev) => ({
      ...prev,
      char_class: value,
      charClass: value,
    }));
  } else {
    setFormData((prev) => ({ ...prev, [name]: value }));
  }
};

  const handleSubmit = (e) => {
    e.preventDefault();
    setCharacter(formData);
    navigate("/character-sheet");
  };

  const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const handleSaveCharacter = async () => {
    const csrfToken = getCookie("csrf_token");

    try {
      const response = await fetch("/api/characters", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.error || "Failed to save character");
      }

      const newCharacter = await response.json();
      setCharacter(newCharacter);
      navigate("/");
    } catch (err) {
      console.error(`Save error: ${err}`);
      alert("Could not save character");
    }
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
                type="text"
                id="name"
                name="name"
                placeholder="Character Name"
                value={formData.name}
                onChange={handleChange}
              />
            </div>

            <RaceSelector onChange={handleChange} />
            <CharClassSelector onChange={handleChange} />
            <BackgroundSelector onChange={handleChange} />

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
            {[
              { label: "Str", name: "strength" },
              { label: "Dex", name: "dexterity" },
              { label: "Con", name: "constitution" },
              { label: "Int", name: "intelligence" },
              { label: "Wis", name: "wisdom" },
              { label: "Cha", name: "charisma" },
            ].map(({ label, name }) => (
              <div className="ability-score" key={name}>
                <label htmlFor={name}>{label}: </label>
                <input
                  type="number"
                  id={name}
                  name={name}
                  min="1"
                  max="20"
                  value={formData[name]}
                  onChange={handleChange}
                />
              </div>
            ))}
          </div>
        </section>

        <section className="section">
          <h2>Appearance & Backstory</h2>
          <p>[Text inputs, textarea, or pickers go here]</p>
        </section>

        <div className="button-group">
          <button type="submit">Preview Character</button>
          <button type="button" onClick={handleSaveCharacter}>
            Save Character
          </button>
        </div>
      </form>
    </div>
  );
}

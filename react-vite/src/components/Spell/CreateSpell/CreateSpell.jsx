import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "./CreateSpell.css";

export default function CreateSpell() {
  const { id: characterId } = useParams();
  console.log("characterId from URL:", characterId);
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    level: 0,
    school: "",
    casting_time: "",
    spell_range: "",
    components: "",
    duration: "",
    description: "",
    higher_levels: ""
  });

  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const res = await fetch("/api/spells/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...formData, character_id: characterId }),
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || "Failed to create spell");
      }

      const newSpell = await res.json();
      navigate(`/character-sheet/${characterId}/spells`);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="create-spell-container">
      <h2>Create New Spell</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit} className="spell-form">
        <label>
          Name:
          <input type="text" name="name" value={formData.name} onChange={handleChange} required />
        </label>

        <label>
          Level:
          <input type="number" name="level" value={formData.level} onChange={handleChange} min="0" />
        </label>

        <label>
          School:
          <input type="text" name="school" value={formData.school} onChange={handleChange} />
        </label>

        <label>
          Casting Time:
          <input type="text" name="casting_time" value={formData.casting_time} onChange={handleChange} />
        </label>

        <label>
          Range:
          <input type="text" name="spell_range" value={formData.spell_range} onChange={handleChange} />
        </label>

        <label>
          Components:
          <input type="text" name="components" value={formData.components} onChange={handleChange} />
        </label>

        <label>
          Duration:
          <input type="text" name="duration" value={formData.duration} onChange={handleChange} />
        </label>

        <label>
          Description:
          <textarea name="description" value={formData.description} onChange={handleChange}></textarea>
        </label>

        <label>
          At Higher Levels:
          <textarea name="higher_levels" value={formData.higher_levels} onChange={handleChange}></textarea>
        </label>

        <button type="submit">Create Spell</button>
      </form>
    </div>
  );
}

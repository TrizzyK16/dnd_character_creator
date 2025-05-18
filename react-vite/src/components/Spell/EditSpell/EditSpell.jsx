import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import "./EditSpell.css";

export default function EditSpell() {
  const { spellId } = useParams();
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
    higher_levels: "",
    character_id: null
  });

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSpell = async () => {
      try {
        const res = await fetch(`/api/spells/${spellId}`);
        if (!res.ok) throw new Error("Failed to fetch spell");
        const data = await res.json();
        setFormData(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSpell();
  }, [spellId]);

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
      const res = await fetch(`/api/spells/${spellId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || "Failed to update spell");
      }

      navigate(`/character-sheet/${formData.character_id}/spells`);
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading) return <p>Loading spell...</p>;

  return (
    <div className="edit-spell-container">
      <h2>Edit Spell</h2>
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

        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
}

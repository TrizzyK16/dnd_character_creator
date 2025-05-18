import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import "./ViewSpell.css";

export default function SpellViewer() {
  const { id: characterId } = useParams();
  const [spells, setSpells] = useState([]);
  const [loading, setLoading] = useState(true);

    const handleDelete = async (spellId) => {
    const confirmDelete = window.confirm("Are you sure you want to delete this spell?");
    if (!confirmDelete) return;

    try {
      const res = await fetch(`/api/spells/${spellId}`, {
        method: "DELETE",
      });

      if (!res.ok) throw new Error("Failed to delete spell");

      setSpells((prev) => prev.filter((spell) => spell.id !== spellId));
    } catch (err) {
      console.error("Error deleting spell:", err);
    }
  };

  useEffect(() => {
    const fetchSpells = async () => {
      try {
        const res = await fetch(`/api/spells/characters/users/${characterId}/characters`);
        if (!res.ok) throw new Error("Failed to fetch spells");

        const data = await res.json();
        setSpells(data);
      } catch (err) {
        console.error("Error loading spells:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchSpells();
  }, [characterId]);

  if (loading) return <p>Loading spells...</p>;

  return (
    <div className="spell-viewer-container">
      <h2>Spells for Character #{characterId}</h2>

      {spells.length === 0 ? (
        <p>No spells found.</p>
      ) : (
        <ul className="spell-list">
          {spells.map(spell => (
            <li key={spell.id} className="spell-card">
              <h3>{spell.name}</h3>
              <p><strong>Level:</strong> {spell.level}</p>
              <p><strong>School:</strong> {spell.school}</p>
              <p><strong>Casting time:</strong> {spell.casting_time}</p>
              <p><strong>Components:</strong> {spell.components}</p>
              <p><strong>Duration:</strong> {spell.duration}</p>
              <p><strong>Description:</strong> {spell.description}</p>
              <p><strong>Higher levels:</strong> {spell.higher_levels}</p>
              
              <div className="spell-buttons">
                <Link to={`/spells/${spell.id}/edit`}>View / Edit</Link>
                <button onClick={() => handleDelete(spell.id)} className="delete-button">Delete</button>
              </div>
            </li>
          ))}
        </ul>
      )}

      <Link to={`/character-sheet/${characterId}/spells/new`} className="create-spell-button">
        Create New Spell
      </Link>
      <Link to={`/character-sheet/${characterId}`} className="back-to-character-sheet">
        ← Back to Character Sheet
        </Link>

    </div>
  );
}

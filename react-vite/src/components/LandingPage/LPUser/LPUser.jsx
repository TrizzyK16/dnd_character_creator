// src/pages/HomePage.jsx
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
import "./LPUser.css";


export default function LPUser() {
  const user = useSelector(state => state.session.user)
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);

  const handleDelete = async (charId) => {
    const confirmed = window.confirm("Are you sure you want to delete this character?");
    if (!confirmed) return;

    try {
      const response = await fetch(`/api/characters/${charId}`, {
        method: 'DELETE',
        credentials: 'include',
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.error || "Failed to delete character");
      }

      // Remove character from local state
      setCharacters(prev => prev.filter(char => char.id !== charId));
      alert("Character deleted!");
    } catch (err) {
      console.error("Delete error:", err);
      alert("Failed to delete character.");
    }
 };


  useEffect(() => {
    if (!user?.id) return;

    const fetchCharacters = async () => {
  try {
    const response = await fetch(`/api/characters/users/${user.id}/characters`);
    if (!response.ok) throw new Error("Failed to fetch");

    const data = await response.json();
    setCharacters(data);
  } catch (error) {
    console.error("Error fetching characters:", error);
  } finally {
    setLoading(false);
  }
};

    fetchCharacters();
  }, [user]);

  if (loading) return <p>Loading your characters...</p>;

  return (
    <div className="home-container">
      <div className="welcome-container">
        <h2>Welcome, {user.username}!</h2>
            <Link to="/builder" className="btn">
              Create a Character
            </Link>
      </div>

      {characters.length > 0 ? (
        <div>
          <h3>Your Characters:</h3>
          <div className="character-grid">
            {characters.map((char) => (
              <div key={char.id} className="character-box">
                <Link to={`/character-sheet/${char.id}`} className="character-name">
                  {char.name}
                </Link>
                <button 
                  onClick={() => handleDelete(char.id)} 
                  className="delete-btn"
                >
                  Delete
                </button>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div>
          <p>You haven&apos;t created any characters yet.</p>
          <Link to="/builder" className="btn">
            Build Your First Character
          </Link>
        </div>
      )}
    </div>
  );
}


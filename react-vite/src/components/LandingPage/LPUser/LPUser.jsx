// src/pages/HomePage.jsx
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
import "./LPUser.css";


export default function LPUser() {
  const user = useSelector(state => state.session.user)
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user?.id) return;

    const fetchCharacters = async () => {
  try {
    const response = await fetch(`/api/users/${user.id}/characters`);
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
      <h2>Welcome, {user.username}!</h2>

      {characters.length > 0 ? (
        <div>
          <h3>Your Characters:</h3>
          <ul>
            {characters.map((char) => (
              <li key={char.id}>
                <Link to={`/characters/${char.id}`}>{char.name}</Link>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <div>
          <p>You haven&apos;t created any characters yet.</p>
          <Link to="/character-builder" className="btn">
            Build Your First Character
          </Link>
        </div>
      )}
    </div>
  );
}


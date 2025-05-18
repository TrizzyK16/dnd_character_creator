import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useCharacter } from "../Context/CharacterContext";
import { useParams } from "react-router-dom";
import "./EditCharacterSheet.css"

export default function EditCharacter() {
    const { id } = useParams();
    const { character, setCharacter } = useCharacter();
    const navigate = useNavigate();

  const [formData, setFormData] = useState(null);

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
      const response = await fetch(`/api/characters/${id}`, {
        method: "PUT",
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

  useEffect(() => {
    if (character) {
      setFormData({
        ...character // overwrite with character values
      });
    }
  }, [character]);

  if (!formData) return null;

  return (
    <div className="sheet-container">
        <form onSubmit={handleSubmit}>
            <header className="sheet-header">
                <h1>Character Sheet</h1>
                <div className="basic-info">
                    <div>
                        <label>Name: </label>
                        <input 
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={(e) => 
                            setFormData({...formData, name: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Level: </label>
                        <input 
                        type="text"
                        name="level"
                        value={formData.level}
                        onChange={(e) => 
                            setFormData({...formData, level: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Alignment: </label>
                        <input 
                        type="text"
                        name="alignment"
                        value={formData.alignment}
                        onChange={(e) => 
                            setFormData({...formData, alignment: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>STR: </label>
                        <input 
                        type="text"
                        name="strength"
                        value={formData.strength}
                        onChange={(e) => 
                            setFormData({...formData, strength: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>DEX: </label>
                        <input 
                        type="text"
                        name="dexterity"
                        value={formData.dexterity}
                        onChange={(e) => 
                            setFormData({...formData, dexterity: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>CON: </label>
                        <input 
                        type="text"
                        name="constitution"
                        value={formData.constitution}
                        onChange={(e) => 
                            setFormData({...formData, constitution: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>INT: </label>
                        <input 
                        type="text"
                        name="intelligence"
                        value={formData.intelligence}
                        onChange={(e) => 
                            setFormData({...formData, intelligence: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>WIS: </label>
                        <input 
                        type="text"
                        name="wisdom"
                        value={formData.wisdom}
                        onChange={(e) => 
                            setFormData({...formData, wisdom: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>CHA: </label>
                        <input 
                        type="text"
                        name="charisma"
                        value={formData.charisma}
                        onChange={(e) => 
                            setFormData({...formData, charisma: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>AC: </label>
                        <input 
                        type="text"
                        name="armor_class"
                        value={formData.armor_class}
                        onChange={(e) => 
                            setFormData({...formData, armor_class: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Initiative: </label>
                        <input 
                        type="text"
                        name="initiative"
                        value={formData.initiative}
                        onChange={(e) => 
                            setFormData({...formData, initiative: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Speed: </label>
                        <input 
                        type="text"
                        name="speed"
                        value={formData.speed}
                        onChange={(e) => 
                            setFormData({...formData, speed: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>HP: </label>
                        <input 
                        type="text"
                        name="hp"
                        value={formData.hp}
                        onChange={(e) => 
                            setFormData({...formData, hp: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Hit Dice: </label>
                        <input 
                        type="text"
                        name="hit_dice"
                        value={formData.hit_dice}
                        onChange={(e) => 
                            setFormData({...formData, hit_dice: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Weapon Proficiencies: </label>
                        <input 
                        type="text"
                        name="weapon_profs"
                        value={formData.weapon_profs}
                        onChange={(e) => 
                            setFormData({...formData, weapon_profs: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Armor Proficiencies: </label>
                        <input 
                        type="text"
                        name="armor_profs"
                        value={formData.armor_profs}
                        onChange={(e) => 
                            setFormData({...formData, armor_profs: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Tool Proficiencies: </label>
                        <input 
                        type="text"
                        name="tool_profs"
                        value={formData.tool_profs}
                        onChange={(e) => 
                            setFormData({...formData, tool_profs: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Languages: </label>
                        <input 
                        type="text"
                        name="languages"
                        value={formData.languages}
                        onChange={(e) => 
                            setFormData({...formData, languages: e.target.value})
                        }
                        />
                    </div>
                    <div>
                        <label>Equipment: </label>
                        <input 
                        type="text"
                        name="equipment"
                        value={formData.equipment}
                        onChange={(e) => 
                            setFormData({...formData, equipment: e.target.value})
                        }
                        />
                    </div>
                </div>
            </header>

            <main className="sheet-body">

            </main>
            <div>
                <button onClick={handleSaveCharacter}>Save Character</button>
            </div>
        </form>
    </div>
  )

}

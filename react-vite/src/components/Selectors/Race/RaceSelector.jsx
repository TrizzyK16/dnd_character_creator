import { useEffect, useState } from 'react';
import "./RaceSelector.css";

export default function RaceSelector({ onChange }) {
  const [raceIndexes, setRaceIndexes] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState('');

  useEffect(() => {
    fetch('/api/races')
      .then((res) => res.json())
      .then((data) => {
        const indexes = data.map((race) => race.index);
        setRaceIndexes(indexes);
      })
      .catch((err) => console.error(`Failed to fetch any races: ${err} 😭`));
  }, []);

  const handleSelectChange = (e) => {
    const value = e.target.value;
    setSelectedIndex(value);
    onChange({ target: { name: "race", value } }); // ✅ send a fake event object
  };

  return (
    <div className="race-selector">
      <label htmlFor="race-select">Select Race: </label>
      <select
        id="race-select"
        value={selectedIndex}
        onChange={handleSelectChange}
      >
        <option value="">-- Select a Race --</option>
        {raceIndexes.map((index) => (
          <option key={index} value={index}>
            {index.charAt(0).toUpperCase() + index.slice(1)}
          </option>
        ))}
      </select>
    </div>
  );
}

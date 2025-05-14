import { useEffect, useState } from 'react';
import "./BackgroundSelector.css";

export default function BackgroundSelector({ onChange }) {
  const [backgroundIndexes, setBackgroundIndexes] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState('');

  useEffect(() => {
    fetch('/api/backgrounds')
      .then((res) => res.json())
      .then((data) => {
        const indexes = data.map((background) => background.index);
        setBackgroundIndexes(indexes);
      })
      .catch((err) => console.error(`Failed to fetch any backgrounds: ${err} 😭`));
  }, []);

  const handleSelectChange = (e) => {
    const value = e.target.value;
    setSelectedIndex(value);
    onChange({ target: { name: "background", value } }); // ✅ send a fake event object
  };

  return (
    <div className="background-selector">
      <label htmlFor="background-select">Select Background: </label>
      <select
        id="background-select"
        value={selectedIndex}
        onChange={handleSelectChange}
      >
        <option value="">-- Select a Background --</option>
        {backgroundIndexes.map((index) => (
          <option key={index} value={index}>
            {index.charAt(0).toUpperCase() + index.slice(1)}
          </option>
        ))}
      </select>
    </div>
  );
}
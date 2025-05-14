import { useEffect, useState } from 'react';
import "./CharClassSelector.css"

export default function CharClassSelector({ onChange }) {
    const [classIndexes, setClassIndexes] = useState([]);
    const [selectedIndex, setSelectedIndex] = useState('');

    // Fetch all class indexes
    useEffect(() => {
        fetch('/api/classes/')
        .then((res) => res.json())
        .then((data) => {
            const indexes = data.map((charClass) => charClass.index);
            setClassIndexes(indexes);
        })
        .catch((err) => console.error(`Failed to fetch any classes: ${err} 😭`));
    }, [])

    const handleSelectChange = (e) => {
        const value = e.target.value;
        setSelectedIndex(value);
        onChange({ target: { name: "charClass", value } })
    }

    return (
        <div className="char-class-selector">
        <label htmlFor="char-class-select">Select Class: </label>
        <select
            id="char-class-select"
            value={selectedIndex}
            onChange={handleSelectChange}
        >
            <option value="">-- Select a Class --</option>
            {classIndexes.map((index) => (
            <option key={index} value={index}>
                {index.charAt(0).toUpperCase() + index.slice(1)} {/* Capitalize */}
            </option>
            ))}
        </select>
        </div>
  );
}

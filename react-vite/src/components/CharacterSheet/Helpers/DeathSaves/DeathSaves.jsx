// DeathSaves.jsx
import { useState } from "react";
import "./DeathSaves.css";

export default function DeathSaves() {
    const [saveCount, setSaveCount] = useState(0);
    const [failCount, setFailCount] = useState(0);

    const toggleCount = (type, index) => {
        if (type === "save") {
            setSaveCount((prev) => (index + 1 === prev ? index : index + 1));
        } else {
            setFailCount((prev) => (index + 1 === prev ? index : index + 1));
        }
    };

    return (
        <>
            <div className="death-save-row">
                <span>Saves:</span>
                <div className="circles">
                    {[0, 1, 2].map((i) => (
                        <div
                            key={`save-${i}`}
                            className={`circle ${i < saveCount ? "filled save" : ""}`}
                            onClick={() => toggleCount("save", i)}
                        />
                    ))}
                </div>
            </div>
            <div className="death-save-row">
                <span>Fails:</span>
                <div className="circles">
                    {[0, 1, 2].map((i) => (
                        <div
                            key={`fail-${i}`}
                            className={`circle ${i < failCount ? "filled fail" : ""}`}
                            onClick={() => toggleCount("fail", i)}
                        />
                    ))}
                </div>
            </div>
        </>
    );
}

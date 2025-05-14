import { createContext, useContext, useState } from "react";

const CharacterContext = createContext();

export function CharacterProvider({ children }) {
    const [character, setCharacter] = useState({});

    return (
        <CharacterContext.Provider value={{character, setCharacter}}>
            {children}
        </CharacterContext.Provider>
    );
}

export function useCharacter() {
    return useContext(CharacterContext);
}
// src/redux/characters.js

// Action Types
const GET_CHARACTERS = 'characters/GET_CHARACTERS';
const ADD_CHARACTER = 'characters/ADD_CHARACTER';
const UPDATE_CHARACTER = 'characters/UPDATE_CHARACTER';
const DELETE_CHARACTER = 'characters/DELETE_CHARACTER';

// Action Creators
const getCharacters = (characters) => ({ type: GET_CHARACTERS, characters });
const addCharacter = (character) => ({ type: ADD_CHARACTER, character });
const updateCharacter = (character) => ({ type: UPDATE_CHARACTER, character });
const deleteCharacter = (characterId) => ({ type: DELETE_CHARACTER, characterId });

function getCSRFToken() {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [name, value] = cookie.trim().split('=');
    if (name === 'csrf_token') return value;
  }
  return null;
}

// Thunk: fetch all characters for current user
export const fetchCharacters = () => async (dispatch) => {
  const res = await fetch('/api/characters');
  if (res.ok) {
    const data = await res.json();
    dispatch(getCharacters(data));
  } else {
    throw new Error('Failed to fetch characters');
  }
};

// Thunk: create a new character
export const createCharacter = (payload) => async (dispatch) => {
  const res = await fetch('/api/characters', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken()
     },
    credentials: 'include',
    body: JSON.stringify(payload),
  });
  if (res.ok) {
    const character = await res.json();
    dispatch(addCharacter(character));
    return character;
  } else {
    throw new Error('Failed to create character');
  }
};

// Thunk: update a character
export const updateCharacterThunk = (characterId, payload) => async (dispatch) => {
  const res = await fetch(`/api/characters/${characterId}`, {
    method: 'PUT',
    headers: { 
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken()
    },
    credentials: 'include',
    body: JSON.stringify(payload),
  });
  if (res.ok) {
    const character = await res.json();
    dispatch(updateCharacter(character));
    return character;
  } else {
    throw new Error('Failed to update character');
  }
};

// Thunk: delete a character
export const deleteCharacterThunk = (characterId) => async (dispatch) => {
  const res = await fetch(`/api/characters/${characterId}`, { 
    method: 'DELETE', 
    headers: {
      'X-CSRFToken': getCSRFToken(),
    },
    credentials: 'include',
  });
  if (res.ok) {
    dispatch(deleteCharacter(characterId));
  } else {
    throw new Error('Failed to delete character');
  }
};

// Initial state
const initialState = {};

// Reducer
const charactersReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_CHARACTERS: {
      const newState = {};
      action.characters.forEach((char) => {
        newState[char.id] = char;
      });
      return newState;
    }
    case ADD_CHARACTER: {
      return {
        ...state,
        [action.character.id]: action.character,
      };
    }
    case UPDATE_CHARACTER: {
      return {
        ...state,
        [action.character.id]: action.character,
      };
    }
    case DELETE_CHARACTER: {
      const newState = { ...state };
      delete newState[action.characterId];
      return newState;
    }
    default:
      return state;
  }
};

export default charactersReducer;

// // Action Types
// const GET_SPELLS = 'spell/GET_SPELLS'
// const ADD_SPELL = 'spell/ADD_SPELL'
// const UPDATE_SPELL = 'spell/UPDATE_SPELL'
// const DELETE_SPELL = 'spell/DELETE_SPELL'

// // Action creators
// const getSpells = (spells) => ({ type: GET_SPELLS, spells });
// const addSpell = (spell) => ({ type: ADD_SPELL, spell });
// const updateSpell = (spell) => ({ type: UPDATE_SPELL, spell });
// const deleteSpell = (spell) => ({ type: DELETE_SPELL, spell });

// function getCSRFToken() {
//     const cookies = document.cookie.split(';');
//     for (let cookie of cookies) {
//         const [name, value] = cookie.trim().split('=');
//         if (name === 'csrf_token') return value;
//     }
//     return null;
// }

// // Thunk: Fetch all spells for current character
// export const fetchSpells = (characterId) => async (dispatch) => {
//     const res = await fetch(`/api/spells/characters/users/${characterId}/character`)
// }
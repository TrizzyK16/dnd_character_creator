import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import LandingPage from '../components/LandingPage/LandingPage';
import CharacterBuilder from '../components/CharacterBuilder/CharacterBuilder';
import CharacterSheet from '../components/CharacterSheet';
// import LoggedInLandingPage from '../components/LandingPage/LPUser/LPUser';
import EditCharacter from '../components/EditCharacterSheet/EditCharacterSheet';
import CreateSpell from '../components/Spell/CreateSpell/CreateSpell';
import SpellViewer from '../components/Spell/ViewSpell/ViewSpell';
import EditSpell from '../components/Spell/EditSpell/EditSpell';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },  
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "/builder",
        element: <CharacterBuilder />
      },
      {
        path: "/character-sheet",
        element: <CharacterSheet />
      },
      {
        path: "/character-sheet/:id",
        element: <CharacterSheet />
      },
      {
        path: "/character-sheet/:id/edit",
        element: <EditCharacter />
      },
      {
        path: "/character-sheet/:id/spells/new",
        element: <CreateSpell />
      },
      {
        path: "/character-sheet/:id/spells",
        element: <SpellViewer />
      },
      {
        path: "/spells/:spellId/edit",
        element: <EditSpell />
      }
    ],
  },
]);
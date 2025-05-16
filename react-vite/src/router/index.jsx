import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import LandingPage from '../components/LandingPage/LandingPage';
import CharacterBuilder from '../components/CharacterBuilder/CharacterBuilder';
import CharacterSheet from '../components/CharacterSheet';
import LoggedInLandingPage from '../components/LandingPage/LPUser/LPUser';

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
      }
    ],
  },
]);
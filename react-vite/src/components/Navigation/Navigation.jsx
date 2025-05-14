import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <nav className="navbar">
      <ul className="nav-list">
        <div>
          <NavLink to="/" className="nav-link">Easy Character Maker</NavLink>
        </div>

        <div className="profile-button">
          <ProfileButton />
        </div>
      </ul>
    </nav>
  );
}

export default Navigation;

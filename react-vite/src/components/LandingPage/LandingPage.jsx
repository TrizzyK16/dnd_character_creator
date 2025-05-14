// src/components/LandingPage.jsx
import { NavLink } from "react-router-dom";
import "./LandingPage.css";

export default function LandingPage() {
  return (
    <div className="landing">
      {/* Hero */}
      <header className="landing-hero">
        <h1>Create and Manage Your D&D Characters with Ease</h1>
        <p>Build sheets, track stats, and level up — all in one place.</p>
        <div className="landing-cta">
          <NavLink to="/signup" className="signup-link">
            Get Started
          </NavLink>
          <NavLink to="/login" className="login-link">
            Log In
          </NavLink>
        </div>
      </header>

      {/* Features */}
      <section className="landing-features">
        <div className="feature">
          <h3>🧙‍♂️ Custom Sheets</h3>
          <p>Design your character exactly how you imagine—race, class, spells, and more.</p>
        </div>
        <div className="feature">
          <h3>⚔️ Track Everything</h3>
          <p>Keep tabs on HP, inventory, proficiencies, and level progression.</p>
        </div>
        <div className="feature">
          <h3>📜 Export & Share</h3>
          <p>Download as PDF or share a public link with your party.</p>
        </div>
      </section>

      {/* Footer CTA */}
      <footer className="landing-footer">
        <p>Ready to roll? Start your next adventure now.</p>
        <NavLink to="/signup" className="signup-link">
          Create Free Account
        </NavLink>
      </footer>
    </div>
  );
}

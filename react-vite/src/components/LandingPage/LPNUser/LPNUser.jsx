// src/components/LandingPage.jsx
import { useModal } from "../../../context/Modal";
import LoginFormModal from "../../LoginFormModal";
import SignupFormModal from "../../SignupFormModal";
import "./LPNUser.css"

export default function LPNUser() {
  const { setModalContent } = useModal();

    const openLoginModal = () => {
      setModalContent(<LoginFormModal />);
    };

    const openSignupModal = () => {
      setModalContent(<SignupFormModal />);
    };

  return (
    <div className="landing">
      {/* Hero */}
      <header className="landing-hero">
        
      </header>
      <div className="create-container">
        <h1>Create and Manage Your D&D Characters with Ease</h1>
        <p>Build sheets, track stats, and level up — all in one place.</p>
        <div className="landing-cta">
          <button onClick={openSignupModal} className="signup-link">
            Get Started
          </button>
          <button onClick={openLoginModal} className="login-link">
            Log In
          </button>
        </div>
      </div>

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
          <h5>(In development...)</h5>
        </div>
      </section>

      {/* Footer CTA */}
      <footer className="landing-footer">
        <p>Ready to roll? Start your next adventure now.</p>
        <button onClick={openSignupModal} className="signup-link">
          Create Free Account
        </button>
      </footer>
    </div>
  );
}

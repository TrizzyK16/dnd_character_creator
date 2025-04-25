import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";
import SignupFormModal from "../SignupFormModal/SignupFormModal"

function LoginFormModal() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal, setModalContent } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
      navigate('/');
    }
  };

  return (
    <div className="login-form-container">
      <div className="login-header">
        <h1>Log In</h1>
      </div>

      <form onSubmit={handleSubmit}>
        <div className="login-form-group">
          <label htmlFor="email">Email</label>
            <input
              id="email"
              className={errors.email ? 'input-error' : ''}
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              placeholder="Please enter your email address :)"
            />
          {errors.email && <div className="error-message">{errors.email}</div>}
        </div>

        <div>
          <label>Password</label>
            <input
              id="password"
              className={errors.password ? 'input-error' : ''}
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="Please enter your password :)"
            />
          {errors.password && <div className="error-message">{errors.password}</div>}
        </div>

        <div className="login-form-actions">
          <button className="login-submit-button" type="submit">Sign In</button>
        </div>

        <div className="login-form-footer">
          <p>Don&apos;t have an acount? 
            <button className="text-button" type="button" onClick={() => {
              closeModal();
              setModalContent(<SignupFormModal />);
            }}>Sign up here!</button>
          </p>
        </div>
      </form>
    </div>
  );
}

export default LoginFormModal;

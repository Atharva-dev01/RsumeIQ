import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h1>ResumeIQ</h1>
      <p>Build a better resume with confidence.</p>

      <Link to="/register">Create Account</Link>
      {" | "}
      <Link to="/login">Login</Link>
    </div>
  );
}

export default Home;
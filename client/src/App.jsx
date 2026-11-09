import { Routes, Route, Link } from "react-router-dom";
import { AuthProvider, useAuth } from "./context/AuthContext.jsx";

import Home from "./pages/Home.jsx";
import Register from "./pages/Register.jsx";
import Login from "./pages/Login.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import ProtectedRoute from "./components/ProtectedRoute.jsx";

function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav>
      <Link to="/">ResumeIQ</Link>
      {" | "}

      {user ? (
        <>
          <Link to="/dashboard">Dashboard</Link>
          {" | "}
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <>
          <Link to="/register">Register</Link>
          {" | "}
          <Link to="/login">Login</Link>
        </>
      )}
    </nav>
  );
}

function App() {
  return (
    <AuthProvider>
      <Navbar />

      <hr />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </AuthProvider>
  );
}

export default App;
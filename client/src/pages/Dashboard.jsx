import { useAuth } from "../context/AuthContext";

function Dashboard() {
  const { user } = useAuth();

  return (
    <div>
      <h1>Welcome, {user?.name}!</h1>
      <p>You are logged in to ResumeIQ.</p>

      <h2>Your Resume Dashboard</h2>
      <p>You will be able to create and manage resumes here next.</p>
    </div>
  );
}

export default Dashboard;
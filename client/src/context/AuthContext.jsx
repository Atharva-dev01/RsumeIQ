import { createContext, useContext, useState } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const savedUser = localStorage.getItem("resumeiqUser");

    return savedUser ? JSON.parse(savedUser) : null;
  });

  const login = (token, userData) => {
    localStorage.setItem("resumeiqToken", token);
    localStorage.setItem("resumeiqUser", JSON.stringify(userData));
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem("resumeiqToken");
    localStorage.removeItem("resumeiqUser");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
import React, { createContext, useContext, useState, useEffect } from "react";
import api from "../services/api";
import type { User } from "../types";

type AuthContextType = {
  user: User | null;
  setUser: (u: User | null) => void;
  logout: () => void;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  async function loadProfile() {
    const token = localStorage.getItem("access_token");
    if (!token) return;
    try {
      const resp = await api.get("/users/me");
      setUser(resp.data);
    } catch {
      setUser(null);
      localStorage.removeItem("access_token");
    }
  }

  useEffect(() => {
    loadProfile();
  }, []);

  function logout() {
    localStorage.removeItem("access_token");
    setUser(null);
  }

  return <AuthContext.Provider value={{ user, setUser, logout }}>{children}</AuthContext.Provider>;
};

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}

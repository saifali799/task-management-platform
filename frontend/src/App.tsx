import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { Dashboard } from "./pages/Dashboard";
import { Tasks } from "./pages/Tasks";
import { AuthProvider } from "./hooks/useAuth";

export default function App() {
  return (
    <AuthProvider>
      <header style={{ padding: 16, borderBottom: "1px solid #ddd" }}>
        <Link to="/">Home</Link> | <Link to="/tasks">Tasks</Link> | <Link to="/login">Login</Link> | <Link to="/register">Register</Link>
      </header>
      <main style={{ padding: 16 }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/tasks" element={<Tasks />} />
        </Routes>
      </main>
    </AuthProvider>
  );
}

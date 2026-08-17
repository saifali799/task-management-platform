import React, { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

export const Register: React.FC = () => {
  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    try {
      await api.post("/auth/register", { email, password, full_name: fullName });
      await api.post("/auth/token", { email, password });
      navigate("/login");
    } catch (err: any) {
      setError(err?.response?.data?.detail || "Registration failed");
    }
  }

  return (
    <div style={{ maxWidth: 480 }}>
      <h2>Register</h2>
      <form onSubmit={submit}>
        <div>
          <label>Email</label>
          <input value={email} onChange={(e) => setEmail(e.target.value)} required />
        </div>
        <div>
          <label>Full name</label>
          <input value={fullName} onChange={(e) => setFullName(e.target.value)} />
        </div>
        <div>
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </div>
        <button type="submit">Register</button>
        {error && <div style={{ color: "red" }}>{error}</div>}
      </form>
    </div>
  );
};

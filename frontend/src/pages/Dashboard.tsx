import React, { useEffect, useState } from "react";
import api from "../services/api";
import { useAuth } from "../hooks/useAuth";

export const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    async function load() {
      try {
        const resp = await api.get("/tasks", { params: { per_page: 1 } });
        setStats({ totalLoaded: resp.data.length });
      } catch {
        setStats({ totalLoaded: 0 });
      }
    }
    load();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      {user ? <p>Welcome, {user.full_name || user.email}</p> : <p>Please log in.</p>}
      <div>
        <strong>Stats</strong>
        <pre>{JSON.stringify(stats, null, 2)}</pre>
      </div>
    </div>
  );
};

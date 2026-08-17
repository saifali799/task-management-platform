import React, { useEffect, useState } from "react";
import api from "../services/api";
import type { Task } from "../types";

export const Tasks: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [q, setQ] = useState("");
  const [loading, setLoading] = useState(false);

  async function load() {
    setLoading(true);
    try {
      const resp = await api.get("/tasks", { params: { q } });
      setTasks(resp.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  return (
    <div>
      <h2>Tasks</h2>
      <div>
        <input placeholder="Search" value={q} onChange={(e) => setQ(e.target.value)} />
        <button onClick={load}>Search</button>
      </div>
      {loading ? (
        <div>Loading...</div>
      ) : (
        tasks.map((t) => (
          <div key={t.id} style={{ border: "1px solid #eee", padding: 8, margin: 6 }}>
            <h3>{t.title}</h3>
            <p>{t.description}</p>
            <small>Status: {t.status} Priority: {t.priority}</small>
          </div>
        ))
      )}
    </div>
  );
};

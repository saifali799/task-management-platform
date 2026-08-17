export type User = {
  id: number;
  email: string;
  full_name?: string;
  created_at?: string;
};

export type Task = {
  id: number;
  title: string;
  description?: string;
  status: "TODO" | "IN_PROGRESS" | "COMPLETED";
  priority: "LOW" | "MEDIUM" | "HIGH";
  due_date?: string | null;
  assignee_id?: number | null;
  created_at?: string;
  updated_at?: string;
};

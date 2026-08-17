# Task Management (3-tier) — Example Application

Overview
- Presentation: React + TypeScript (frontend/)
- Application: FastAPI + SQLAlchemy + Alembic (backend/)
- Data: PostgreSQL with migrations (backend/migrations/)

Quick start (development)
1. Copy .env.example to .env and fill values:
   cp .env.example .env

2. Backend
   python3 -m venv backend/.venv
   source backend/.venv/bin/activate
   pip install -r backend/requirements.txt
   # Run migrations with a real PostgreSQL DB (set DATABASE_URL)
   # alembic -c backend/alembic.ini upgrade head
   uvicorn app.main:app --reload --port 8000

3. Frontend
   cd frontend
   npm install
   npm run dev

Testing
- Backend tests use an in-memory SQLite DB and can be run with:
  cd backend
  source .venv/bin/activate
  pytest

- Frontend tests use Vitest if Node is installed.

Notes
- Do not commit real secrets. Use environment variables.
- The provided .env.example contains placeholders only.

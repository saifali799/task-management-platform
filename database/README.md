Database helpers:
- Alembic migration files are in backend/migrations
- To run migrations with PostgreSQL, set DATABASE_URL and run:
  alembic -c backend/alembic.ini upgrade head

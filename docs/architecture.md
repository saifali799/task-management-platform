3-tier architecture:
- Presentation: React calls REST endpoints under /api/*
- Application: FastAPI provides REST, performs authentication, validation, business logic
- Data: PostgreSQL with schema and constraints, accessed via SQLAlchemy ORM

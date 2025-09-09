from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 1. Database URL
# Example: For PostgreSQL
# postgresql://<username>:<password>@<host>/<database_name>
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# 2. SQLAlchemy Engine
# 'connect_args' is only needed for SQLite
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

# 3. SessionLocal: each request gets its own DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class for models
Base = declarative_base()

# 5. Dependency for FastAPI routes


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

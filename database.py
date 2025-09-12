from sqlalchemy import create_engine
from urllib.parse import quote
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Database connection parameters
driver_name = '{ODBC Driver 18 for SQL Server}'
server_name = 'vaibhav-database-server-2'
database_name = 'task-manager'
password = 'Winning@11'
username = 'ParnoidAndroid'

connection_string = 'Driver={};Server=tcp:{}.database.windows.net,1433;Database={};Uid={};Pwd={};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'.format(
    driver_name, server_name, database_name, username, password)

# 2. Create SQLAlchemy engine
params = quote(connection_string)
url = "mssql+pyodbc:///?odbc_connect={0}".format(params)
engine = create_engine(url)

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

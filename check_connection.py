from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

connection_string = (
    "mssql+pyodbc://vaibhav.motwani@students.unibe.ch@vaibhav-database-server/"
    "task-manager?"
    "driver=ODBC+Driver+18+for+SQL+Server&"
    "authentication=ActiveDirectoryIntegrated"
)

# DATABASE_URL = os.getenv("AZURE_SQL_CONNECTION_STRING")
# print("Database URL:", DATABASE_URL)

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Test connection
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connection successful!" if result.scalar()
              == 1 else "Connection test failed!")
except SQLAlchemyError as e:
    print("Connection failed:", e)

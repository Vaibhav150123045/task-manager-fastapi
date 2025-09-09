from sqlalchemy import create_engine, text
from azure.identity import DefaultAzureCredential
import urllib


class SQLAlchemyConnector:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.credential = DefaultAzureCredential()

    def get_connection_string(self):
        """Generate connection string with access token"""
        token = self.credential.get_token(
            "https://database.windows.net/.default").token

        conn_str = (
            f"Driver={{ODBC Driver 18 for SQL Server}};"
            f"Server={self.server};"
            f"Database={self.database};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"AccessToken={token};"
        )

        return f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(conn_str)}"

    def get_engine(self):
        """Create SQLAlchemy engine"""
        connection_string = self.get_connection_string()
        return create_engine(connection_string)

    def test_connection(self):
        """Test the database connection"""
        try:
            engine = self.get_engine()
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                print("Connection successful!")
                return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False


# Usage
if __name__ == "__main__":
    connector = SQLAlchemyConnector(
        server="tcp:vaibhav-database-server-2.database.windows.net",
        database="task-manager"
    )
    connector.test_connection()

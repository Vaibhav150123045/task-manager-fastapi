import pyodbc
from azure.identity import DefaultAzureCredential
# Define your connection parameters
server = 'tcp:vaibhav-database-server.database.windows.net,1433'
database = 'task-manager'
driver = '{ODBC Driver 18 for SQL Server}'
# Get a token using Azure Identity
credential = DefaultAzureCredential()
token = credential.get_token("https://database.windows.net/.default")
# Create a connection string
connection_string = f"Driver={driver};Server={server};Database={database};Authentication=ActiveDirectoryAccessToken;UID=;PWD={token.token};"
# Connect to the database
with pyodbc.connect(connection_string) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print(row)

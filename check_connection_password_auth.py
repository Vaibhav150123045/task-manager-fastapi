import pyodbc

# Define connection parameters
server = 'vaibhav-database-server-2.database.windows.net'
database = 'task-manager'
username = 'ParnoidAndroid'
password = 'Winning@11'  # replace with your actual password
driver = '{ODBC Driver 18 for SQL Server}'

# Create the connection string
connection_string = f"""
    DRIVER={driver};
    SERVER=tcp:{server},1433;
    DATABASE={database};
    UID={username};
    PWD={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
"""

with pyodbc.connect(connection_string) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print(row)

import pyodbc
server = 'vaibhav-database-server.database.windows.net'
database = 'task-manager'  # Replace with your database name
username = 'CloudSA5d14747a'  # Replace with your username
conn = pyodbc.connect(
    f'Driver={{ODBC Driver 18 for SQL Server}};'
    f'Server=tcp:{server},1433;'
    f'Database={database};'
    f'Uid={username};'
    f'Encrypt=yes;'
    f'TrustServerCertificate=no;'
    f'Connection Timeout=30;'
    f'Authentication=ActiveDirectoryIntegrated;'
)
cursor = conn.cursor()

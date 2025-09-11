import pyodbc
from urllib.parse import quote
from sqlalchemy import create_engine, text

# Define connection parameters
server = 'vaibhav-database-server-2.database.windows.net'
database = 'task-manager'
username = 'ParnoidAndroid'
password = 'Winning@11'  # replace with your actual password
driver = '{ODBC Driver 18 for SQL Server}'

# Create the connection string
# params = quote_plus(f"""
#     SERVER=tcp:{server},1433;
#     DATABASE={database};
#     UID={username};
#     PWD={password};
#     DRIVER={driver};
#     Encrypt=yes;
#     TrustServerCertificate=no;
#     Connection Timeout=30;
# """)

# params = quote_plus('Driver={};Server=tcp:{}.database.windows.net,1433;Database={};Uid=ParnoidAndroid;Pwd=Winning@11;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'.format(//driver_name, server_name, database_name))

# connection_string = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

driver_name = '{ODBC Driver 18 for SQL Server}'
server_name = 'vaibhav-database-server-2'
database_name = 'task-manager'
password = 'Winning@11'
username = 'ParnoidAndroid'

connection_string = 'Driver={};Server=tcp:{}.database.windows.net,1433;Database={};Uid={};Pwd={};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'.format(
    driver_name, server_name, database_name, username, password)


def get_engine():
    params = quote(connection_string)
    url = "mssql+pyodbc:///?odbc_connect={0}".format(params)
    return create_engine(url)


engine = get_engine()

with engine.connect() as conn:
    result = conn.execute(text("SELECT @@VERSION;"))
    print(result.fetchone())

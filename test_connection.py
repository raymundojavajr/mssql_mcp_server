import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

print("Attempting to connect via pyodbc...")

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('MSSQL_SERVER')};"
        f"DATABASE={os.getenv('MSSQL_DATABASE')};"
        f"UID={os.getenv('MSSQL_USER')};"
        f"PWD={os.getenv('MSSQL_PASSWORD')};"
    )
    print("✅ pyodbc connection successful!")

    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 * FROM INFORMATION_SCHEMA.TABLES")
    row = cursor.fetchone()
    print(f"🧪 Query result: {row}")

    cursor.close()
    conn.close()
    print("✅ Connection test completed successfully!")
except Exception as e:
    print("❌ Error:", e)

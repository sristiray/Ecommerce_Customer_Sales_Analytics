import sqlite3
import pandas as pd

# CSV file
csv_file = "data/ecommerce_sales.csv"

# SQLite database
db_file = "ecommerce.db"

# Read CSV
df = pd.read_csv(csv_file)

# Connect to SQLite
conn = sqlite3.connect(db_file)

# Import data into SQLite
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("CSV imported successfully!")
print("Total rows:", len(df))
import sqlite3

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT
    City,
    ROUND(SUM(Total_Amount), 2) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC;
"""

print("=== CITY-WISE REVENUE ===")

for row in conn.execute(query):
    print(row[0], ":", row[1])

conn.close()
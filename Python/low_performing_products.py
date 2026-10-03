import sqlite3

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT
    Product,
    SUM(Quantity) AS Units_Sold,
    ROUND(SUM(Total_Amount), 2) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue ASC
LIMIT 10;
"""

print("=== LOW-PERFORMING PRODUCTS ===")

for row in conn.execute(query):
    print(
        row[0],
        "| Units Sold:", row[1],
        "| Revenue:", row[2]
    )

conn.close()

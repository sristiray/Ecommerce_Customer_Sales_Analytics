import sqlite3

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Total_Amount), 2) AS Revenue
FROM sales
GROUP BY Payment_Method
ORDER BY Revenue DESC;
"""

print("=== PAYMENT METHOD ANALYSIS ===")

for row in conn.execute(query):
    print(
        row[0],
        "| Orders:", row[1],
        "| Revenue:", row[2]
    )

conn.close()